import sys
import time

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = int(open(filename).read().strip())

    def part1(self):
        houses = [0 for _ in range(self.data // 10)]

        for elf in range(1, len(houses)):
            for house in range(elf, len(houses), elf):
                houses[house] += elf * 10

        for i, presents in enumerate(houses):
            if presents >= self.data:
                return i

    def part2(self):
        houses = [0 for _ in range(self.data // 10)]

        for elf in range(1, len(houses)):
            for house in range(elf, min(len(houses), elf * 50), elf):
                houses[house] += elf * 11

        for i, presents in enumerate(houses):
            if presents >= self.data:
                return i


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
