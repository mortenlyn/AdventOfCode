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
        self.weapons = {
            "dagger": (8, 4),
            "shortsword": (10, 5),
            "warhammer": (25, 6),
            "longsword": (40, 7),
            "greataxe": (74, 8),
        }

        self.armor = {
            "leather": (13, 1),
            "chainmail": (31, 2),
            "splintmail": (53, 3),
            "bandedmail": (75, 4),
            "platemail": (102, 5),
        }

        self.rings = {
            "damage +1": (25, 1, 0),
            "damage +2": (50, 2, 0),
            "damage +3": (100, 3, 0),
            "defense +1": (20, 0, 1),
            "defense +2": (40, 0, 2),
            "defense +3": (80, 0, 3),
        }

        self.boss_hp = 109
        self.boss_damage = 8
        self.boss_armor = 2

    def fight(self, player_damage, player_armor):
        player_turn = True
        boss_hp = self.boss_hp
        player_hp = 100

        while True:
            if player_turn:
                damage = player_damage - self.boss_armor
                damage = max(damage, 1)
                boss_hp -= damage
                if boss_hp <= 0:
                    return True
            else:
                damage = self.boss_damage - player_armor
                damage = max(damage, 1)
                player_hp -= damage
                if player_hp <= 0:
                    return False

            player_turn = not player_turn

    def part1(self):
        min_cost = float("inf")

        for weapon in self.weapons:
            player_damage = 0
            player_armor = 0
            cost = 0

            player_damage = self.weapons[weapon][1]

            if self.fight(player_damage, player_armor):
                min_cost = min(min_cost, self.weapons[weapon][0])

            for armor in self.armor:
                player_damage = self.weapons[weapon][1]

                player_armor = self.armor[armor][1]

                cost = self.weapons[weapon][0]
                cost += self.armor[armor][0]

                if self.fight(player_damage, player_armor):
                    min_cost = min(min_cost, cost)

                for ring in self.rings:
                    player_damage = self.weapons[weapon][1]
                    player_damage += self.rings[ring][1]

                    player_armor = self.armor[armor][1]
                    player_armor += self.rings[ring][2]

                    cost = self.weapons[weapon][0]
                    cost += self.armor[armor][0]
                    cost += self.rings[ring][0]

                    if self.fight(player_damage, player_armor):
                        min_cost = min(min_cost, cost)

                for ring1, ring2 in itertools.combinations(self.rings, 2):
                    player_damage = self.weapons[weapon][1]
                    player_damage += self.rings[ring1][1]
                    player_damage += self.rings[ring2][1]

                    player_armor = self.armor[armor][1]
                    player_armor += self.rings[ring1][2]
                    player_armor += self.rings[ring2][2]

                    cost = self.weapons[weapon][0]
                    cost += self.armor[armor][0]
                    cost += self.rings[ring1][0]
                    cost += self.rings[ring2][0]

                    if self.fight(player_damage, player_armor):
                        min_cost = min(min_cost, cost)

        return min_cost

    def fight_with_boss_items(
        self, player_damage, player_armor, boss_damage, boss_armor
    ):
        player_turn = True
        boss_hp = self.boss_hp
        player_hp = 100

        while True:
            if player_turn:
                damage = player_damage - boss_armor
                damage = max(damage, 1)
                boss_hp -= damage
                if boss_hp <= 0:
                    return True
            else:
                damage = boss_damage - player_armor
                damage = max(damage, 1)
                player_hp -= damage
                if player_hp <= 0:
                    return False

            player_turn = not player_turn

    def part2(self):
        max_cost = 0

        for weapon in self.weapons:
            for armor in self.armor:
                for ring in itertools.chain(
                    self.rings, itertools.combinations(self.rings, 2)
                ):
                    if len(ring) == 2:
                        player_damage = self.weapons[weapon][1] + sum(
                            self.rings[ring][1] for ring in ring
                        )
                        player_armor = self.armor[armor][1] + sum(
                            self.rings[ring][2] for ring in ring
                        )
                        player_cost = (
                            self.weapons[weapon][0]
                            + self.armor[armor][0]
                            + sum(self.rings[ring][0] for ring in ring)
                        )
                    else:
                        player_damage = self.weapons[weapon][1] + self.rings[ring][1]
                        player_armor = self.armor[armor][1] + self.rings[ring][2]
                        player_cost = (
                            self.weapons[weapon][0]
                            + self.armor[armor][0]
                            + self.rings[ring][0]
                        )

                    for b_weapon in self.weapons:
                        if b_weapon == weapon:
                            continue
                        for b_armor in self.armor:
                            if b_armor == armor:
                                continue
                            for b_ring in itertools.chain(
                                self.rings, itertools.combinations(self.rings, 2)
                            ):

                                if len(b_ring) == 2:
                                    if ring in b_ring:
                                        continue
                                    boss_damage = (
                                        self.boss_damage
                                        + self.weapons[b_weapon][1]
                                        + sum(self.rings[ring][1] for ring in b_ring)
                                    )
                                    boss_armor = (
                                        self.boss_armor
                                        + self.armor[b_armor][1]
                                        + sum(self.rings[ring][2] for ring in b_ring)
                                    )
                                else:
                                    if b_ring == ring:
                                        continue
                                    boss_damage = (
                                        self.boss_damage
                                        + self.weapons[b_weapon][1]
                                        + self.rings[b_ring][1]
                                    )
                                    boss_armor = (
                                        self.boss_armor
                                        + self.armor[b_armor][1]
                                        + self.rings[b_ring][2]
                                    )

                                if not self.fight_with_boss_items(
                                    player_damage, player_armor, boss_damage, boss_armor
                                ):
                                    max_cost = max(max_cost, player_cost)

        return max_cost


def main():
    start = time.perf_counter()

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2015, 21, None, part2)


if __name__ == "__main__":
    main()
