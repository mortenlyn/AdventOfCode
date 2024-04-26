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
        self.prereq_overview = defaultdict(list)

        for line in self.data:
            words = line.split()
            self.prereq_overview[words[7]].append(words[1])
            self.prereq_overview[words[1]]

    def part1(self):
        result = ""

        while self.prereq_overview:
            next_step = min(
                [
                    step
                    for step, prereqs in self.prereq_overview.items()
                    if len(prereqs) == 0
                ]
            )
            result += next_step
            del self.prereq_overview[next_step]
            for prereqs in self.prereq_overview.values():
                if next_step in prereqs:
                    prereqs.remove(next_step)

        return result

    def part2(self):
        pass


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")
    # quit()
    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2018, 7, None, part2)


if __name__ == "__main__":
    main()
