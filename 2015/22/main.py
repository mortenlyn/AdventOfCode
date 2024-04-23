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

    def simulate_turn(
        self,
        player_hp,
        player_mana,
        player_damage,
        player_armor,
        boss_hp,
        total_mana_used,
        effects,
        spell_name,
    ):

        for effect in effects:
            if effect["name"] == "shield":
                player_armor = 7
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)
            if effect["name"] == "poison":
                boss_hp -= 3
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)
            if effect["name"] == "recharge":
                player_mana += 101
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)

        spell_info = self.spells[spell_name]
        player_mana -= spell_info[0]
        total_mana_used += spell_info[0]

        if spell_info[1] > 0:
            boss_hp -= spell_info[1]
        if spell_info[2] > 0:
            player_hp += spell_info[2]
        if spell_name == "shield":
            effects.append({"name": "shield", "timer": 6})
        if spell_name == "poison":
            effects.append({"name": "poison", "timer": 6})
        if spell_name == "recharge":
            effects.append({"name": "recharge", "timer": 5})

        return (
            player_hp,
            player_mana,
            player_damage,
            player_armor,
            boss_hp,
            total_mana_used,
            effects,
        )

    def boss_attack(
        self,
        player_hp,
        player_mana,
        player_damage,
        player_armor,
        boss_hp,
        total_mana_used,
        effects,
    ):
        for effect in effects:
            if effect["name"] == "shield":
                player_armor = 7
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)
            if effect["name"] == "poison":
                boss_hp -= 3
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)
            if effect["name"] == "recharge":
                player_mana += 101
                effect["timer"] -= 1
                if effect["timer"] == 0:
                    effects.remove(effect)

        if boss_hp <= 0:
            return (
                True,
                player_hp,
                player_mana,
                player_damage,
                player_armor,
                boss_hp,
                total_mana_used,
                effects,
            )

        damage = max(self.boss_stats["damage"] - player_armor, 1)
        return (
            False,
            player_hp - damage,
            player_mana,
            player_damage,
            player_armor,
            boss_hp,
            total_mana_used,
            effects,
        )

    def dfs(
        self,
        player_hp,
        player_mana,
        player_damage,
        player_armor,
        boss_hp,
        total_mana_used,
        effects,
    ):

        if boss_hp <= 0:
            return total_mana_used

        min_mana = float("inf")
        for spell_name, spell_info in self.spells.items():
            if player_mana >= spell_info[0]:
                if not any(effect["name"] == spell_name for effect in effects):
                    (
                        new_player_hp,
                        new_player_mana,
                        new_player_damage,
                        new_player_armor,
                        new_boss_hp,
                        new_total_mana_used,
                        new_effects,
                    ) = self.simulate_turn(
                        player_hp,
                        player_mana,
                        player_damage,
                        player_armor,
                        boss_hp,
                        total_mana_used,
                        effects.copy(),
                        spell_name,
                    )

                    if new_boss_hp <= 0:
                        return new_total_mana_used

                    (
                        win_info,
                        new_player_hp,
                        new_player_mana,
                        new_player_damage,
                        new_player_armor,
                        new_boss_hp,
                        new_total_mana_used,
                        new_effects,
                    ) = self.boss_attack(
                        new_player_hp,
                        new_player_mana,
                        new_player_damage,
                        new_player_armor,
                        new_boss_hp,
                        new_total_mana_used,
                        new_effects,
                    )

                    if win_info:
                        return new_total_mana_used

                    if new_player_hp > 0:
                        min_mana = min(
                            min_mana,
                            self.dfs(
                                new_player_hp,
                                new_player_mana,
                                new_player_damage,
                                new_player_armor,
                                new_boss_hp,
                                new_total_mana_used,
                                new_effects,
                            ),
                        )

        return min_mana

    def min_mana_cost(self):
        min_mana = self.dfs(
            self.player_stats["hp"],
            self.player_stats["mana"],
            self.player_stats["damage"],
            self.player_stats["armor"],
            self.boss_stats["hp"],
            0,
            [],
        )
        return min_mana

    def part1(self):
        return self.min_mana_cost()

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")
    # quit()
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
