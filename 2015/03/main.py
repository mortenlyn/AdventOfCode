import sys
import time
from collections import defaultdict

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [*open(filename).read().rstrip()]

    def determine_instruction(self, instruction, x, y):
        match instruction:
            case ">":
                return x + 1, y
            case "<":
                return x - 1, y
            case "^":
                return x, y + 1
            case "v":
                return x, y - 1

    def part1(self):
        houses = defaultdict(int)
        x = y = 0

        for instruction in self.data:
            houses[(x, y)] += 1
            x, y = self.determine_instruction(instruction, x, y)

        return len(houses)

    def part2(self):
        houses = defaultdict(int)
        x1 = y1 = x2 = y2 = 0

        for i in range(0, len(self.data), 2):
            houses[(x1, y1)] += 1
            x1, y1 = self.determine_instruction(self.data[i], x1, y1)

        for i in range(1, len(self.data), 2):
            houses[(x2, y2)] += 1
            x2, y2 = self.determine_instruction(self.data[i], x2, y2)

        return len(houses)


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
