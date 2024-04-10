import functools
import itertools
import os
import re
import string
import sys
import time
from collections import defaultdict, deque
from pprint import pprint

sys.path.insert(0, "../../")
from utils import copy_answer, request_submit, write_solution


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            parseLine(line) for line in open(filename).read().rstrip().split("\n")
        ]

        # (Manacost, damage, heal, armor, mana-regen, effect-rounds)
        self.spells = {
            "magic_missile": [53, 4, 0, 0, 0, 0, False],
            "drain": [73, 2, 2, 0, 0, 0, False],
            "shield": [113, 0, 6, 7, 0, 6, False],
            "poison": [173, 3, 0, 0, 0, 6, False],
            "recharge": [229, 0, 0, 0, 101, 0, False],
        }

        self.boss_stats = {"hp": 71, "damage": 10}

        self.player_stats = {"hp": 50, "mana": 500, "damage": 0, "armor": 0}

    def fight(self, player_damage, player_armor):
        for spell_name, spell_info in self.spells.items():
            if spell_info[-1]:
                self.player_stats["damage"] += spell_info[1]
                self.player_stats["armor"] += spell_info[3]
                self.player_stats["mana"] += spell_info[4]

        player_turn = True

        self.boss_stats["hp"] = 71
        self.player_stats["hp"] = 50

        while True:
            if player_turn:
                damage = player_damage
                damage = max(damage, 1)
                self.boss_stats["hp"] -= damage
                if self.boss_stats["hp"] <= 0:
                    return True
            else:
                damage = self.boss_stats["damage"] - player_armor
                damage = max(damage, 1)
                self.player_stats["hp"] -= damage
                if self.player_stats["hp"] <= 0:
                    return False

            player_turn = not player_turn

    def decrement_effect_timer(self):
        for spell_name, spell_info in self.spells.items():
            if spell_info[-1]:
                self.spells[spell_name][-2] -= 1

            if spell_info[-2] == 0:
                self.spells[spell_name][-2] = False

    def mana_cost(self):
        min_mana = 0

        return min_mana

    def part1(self):
        return self.mana_cost()

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2015, 22, part1, part2)


if __name__ == "__main__":
    main()
