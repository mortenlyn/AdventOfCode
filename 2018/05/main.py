import sys
import time
from collections import defaultdict, deque
from pprint import pprint

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
        polymer = list(self.data[0])

        i = 0
        while i < len(polymer) - 1:
            if polymer[i].swapcase() == polymer[i + 1]:
                del polymer[i : i + 2]
                i = max(0, i - 1)
            else:
                i += 1

        return len(polymer)

    def part2(self):
        polymer = list(self.data[0])

        min_length = float("inf")

        for letter in set(self.data[0].lower()):
            modified_polymer = (
                "".join(polymer).replace(letter, "").replace(letter.upper(), "")
            )

            modified_polymer = list(modified_polymer)

            i = 0
            while i < len(modified_polymer) - 1:
                if modified_polymer[i].swapcase() == modified_polymer[i + 1]:
                    del modified_polymer[i : i + 2]
                    i = max(0, i - 1)
                else:
                    i += 1
            min_length = min(min_length, len(modified_polymer))

        return min_length


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
