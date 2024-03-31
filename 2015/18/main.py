import functools
import itertools
import os
import re
import string
import sys
import time
from collections import Counter, defaultdict, deque
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

    def decide_next_state(self, i, j):
        num_rows = len(self.data)
        num_cols = len(self.data[0])

        if self.data[i][j] == "#":
            return (
                "#"
                if sum(
                    1
                    for x in range(max(0, i - 1), min(num_rows, i + 2))
                    for y in range(max(0, j - 1), min(num_cols, j + 2))
                    if self.data[x][y] == "#"
                )
                in [2, 3]
                else "."
            )
        else:
            return (
                "#"
                if sum(
                    1
                    for x in range(max(0, i - 1), min(num_rows, i + 2))
                    for y in range(max(0, j - 1), min(num_cols, j + 2))
                    if self.data[x][y] == "#"
                )
                == 3
                else "."
            )

    def part1(self):
        result = self.data.copy()

        for _ in range(4):
            for i in range(len(result)):
                for j in range(len(result[0])):
                    result[i] = (
                        result[i][:j]
                        + self.decide_next_state(i, j)
                        + result[i][j + 1 :]
                    )
        return Counter(itertools.chain(*result))["#"]

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == 6 else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    # solution = Solution()
    # part1 = solution.part1()
    # part2 = solution.part2()
    # print(part1_text := f"Part 1: {part1}")
    # print(part2_text := f"Part 2: {part2}")

    # print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    # copy_answer(part1, part2)
    # write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    # request_submit(2015, 18, part1, part2)


if __name__ == "__main__":
    main()
