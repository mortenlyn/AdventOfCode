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
        result = 0
        for frequency in self.data:
            if frequency[0] == "+":
                result += int(frequency[1:])
            else:
                result -= int(frequency[1:])

        return result

    def part2(self):
        frequencies = set()
        result = 0

        while True:
            for frequency in self.data:
                if frequency[0] == "+":
                    result += int(frequency[1:])

                    if result in frequencies:
                        return result

                    frequencies.add(result)
                else:
                    result -= int(frequency[1:])
                    if result in frequencies:
                        return result

                    frequencies.add(result)


def main():
    start = time.perf_counter()

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2018, 1, None, part2)


if __name__ == "__main__":
    main()
