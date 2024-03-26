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

    def part1(self):
        for i in range(len(self.data)):
            self.data[i] = re.split(r": |, ", self.data[i])

        info = {}

        for i in range(len(self.data)):
            for j in range(1, len(self.data[i][1:])):
                key = self.data[i][j][0:-2].strip()
                if key in info:
                    info[key].append(self.data[i][j][-2:].strip())
                else:
                    info[key] = [self.data[i][j][-2:].strip()]

        ingredients = [ingr for ingr in info.keys()]

        teaspoons = 100
        max_score = 0

        for i in range(len(info.keys()) - 1):
            for j in range(len(info[ingredients[0]])):
                for k in range(teaspoons + 1):
                    print(info[i][j], k)

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    # solution = Solution()
    # part1 = solution.part1()
    # part2 = solution.part2()
    # print(part1_text := f"Part 1: {part1}")
    # print(part2_text := f"Part 2: {part2}")

    # print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    # copy_answer(part1, part2)
    # write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    # request_submit(2015, 15, part1, part2)


if __name__ == "__main__":
    main()
