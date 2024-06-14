import os
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

    def calculate_paper(self, l, w, h):
        lw = l * w
        wh = w * h
        hl = h * l
        return 2 * lw + 2 * wh + 2 * hl + min(lw, wh, hl)

    def part1(self):
        square_feet = 0

        for line in self.data:
            numbers = line.split("x")
            numbers = list(map(int, numbers))
            square_feet += self.calculate_paper(*numbers)

        return square_feet

    def calculate_ribbon(self, l, w, h):
        return 2 * sum(sorted([l, w, h])[:2]) + l * w * h

    def part2(self):
        ribbon = 0

        for line in self.data:
            numbers = line.split("x")
            numbers = list(map(int, numbers))
            ribbon += self.calculate_ribbon(*numbers)

        return ribbon


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
