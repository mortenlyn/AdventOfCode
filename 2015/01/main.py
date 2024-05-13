import sys
import time

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(filename).read().rstrip()

    def part1(self):
        floor = 0

        for letter in self.data:
            if letter == "(":
                floor += 1
            else:
                floor -= 1

        return floor

    def part2(self):
        floor = 0

        for i, letter in enumerate(self.data):
            if letter == "(":
                floor += 1
            else:
                floor -= 1

            if floor == -1:
                return i + 1


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
