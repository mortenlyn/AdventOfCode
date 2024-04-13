import itertools
import sys
import time

sys.path.insert(0, "../../")


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
            "fill_armor": (0, 0),
        }

        self.rings = {
            "damage +1": (25, 1, 0),
            "damage +2": (50, 2, 0),
            "damage +3": (100, 3, 0),
            "defense +1": (20, 0, 1),
            "defense +2": (40, 0, 2),
            "defense +3": (80, 0, 3),
            "fill_ring1": (0, 0, 0),
            "fill_ring2": (0, 0, 0),
        }

        self.boss_stats = {"hp": 100, "damage": 8, "armor": 2}

        self.player_stats = {"hp": 100, "damage": 0, "armor": 0}

    def fight(self, player_damage, player_armor):
        player_turn = True
        self.boss_stats["hp"] = 109
        self.player_stats["hp"] = 100

        while True:
            if player_turn:
                damage = player_damage - self.boss_stats["armor"]
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

    def shop(self):
        for weapon_name, weapon_stats in self.weapons.items():
            for armor_name, armor_stats in self.armor.items():
                for (ring1_name, ring1_stats), (
                    ring2_name,
                    ring2_stats,
                ) in itertools.combinations(self.rings.items(), 2):
                    yield (
                        self.fight(
                            sum(
                                [
                                    weapon_stats[1],
                                    ring1_stats[1],
                                    ring2_stats[1],
                                ]
                            ),
                            sum([armor_stats[1], ring1_stats[2], ring2_stats[2]]),
                        ),
                        sum(
                            [
                                weapon_stats[0],
                                armor_stats[0],
                                ring1_stats[0],
                                ring2_stats[0],
                            ]
                        ),
                    )

    def part1(self):
        return min(price for win, price in self.shop() if win)

    def part2(self):
        return max(price for win, price in self.shop() if not win)


def main():
    start = time.perf_counter()

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


if __name__ == "__main__":
    main()
