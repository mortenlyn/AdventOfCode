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

    def manhattenDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def part1(self):
        coords = [tuple(map(int, line.split(", "))) for line in self.data]
        min_x = min(x for x, y in coords)
        max_x = max(x for x, y in coords)
        min_y = min(y for x, y in coords)
        max_y = max(y for x, y in coords)

        grid = {}
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                distances = sorted(
                    (
                        (self.manhattenDistance(x, y, cx, cy), i)
                        for i, (cx, cy) in enumerate(coords)
                    )
                )
                if distances[0][0] != distances[1][0]:
                    grid[x, y] = distances[0][1]
        print(grid)

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")
    quit()
    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2018, 6, part1, part2)


if __name__ == "__main__":
    main()
