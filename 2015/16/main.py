import re
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

    def part1(self):
        sue_overview = {}

        wanted_items = [
            "children: 3",
            "cats: 7",
            "samoyeds: 2",
            "pomeranians: 3",
            "akitas: 0",
            "vizslas: 0",
            "goldfish: 5",
            "trees: 3",
            "cars: 2",
            "perfumes: 1",
        ]

        for line in self.data:
            sue = "".join(re.findall(r"\d+:", line))[:-1]
            items = re.findall(r"\w+: \d+", line)
            sue_overview[sue] = items

        for sue, items in sue_overview.items():
            if all(item in wanted_items for item in items):
                return sue

    def part2(self):
        sue_overview = {}

        wanted_items = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }

        for line in self.data:
            sue = "".join(re.findall(r"\d+:", line))[:-1]
            items = re.findall(r"\w+: \d+", line)
            sue_overview[sue] = items

        for sue, items in sue_overview.items():
            for item in items:
                key, value = item.split(": ")
                if key in wanted_items:
                    if key in ["cats", "trees"]:
                        if int(value) <= wanted_items[key]:
                            break
                    elif key in ["pomeranians", "goldfish"]:
                        if int(value) >= wanted_items[key]:
                            break
                    else:
                        if int(value) != wanted_items[key]:
                            break
            else:
                return sue


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
