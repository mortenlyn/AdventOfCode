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
        self.mapping = defaultdict(list)
        self.replacements = self.data[:-2]

        for line in self.replacements:
            atom, replacement = line.split(" => ")

            self.mapping[atom].append(replacement)

        self.molecule = list(re.findall(r"[A-Z][a-z]*", self.data[-1]))

    def part1(self):
        results = set()

        for i in range(len(self.molecule)):
            for replacement in self.mapping[self.molecule[i]]:
                temp = self.molecule.copy()
                temp[i] = replacement
                results.add("".join(temp))

        return len(results)

    # def replace(self, index, reverse_molecule):
    #     atom = reverse_molecule[index]
    #     counter = index

    #     for key, value in self.mapping.items():
    #         counter += 1
    #         if atom in value:
    #             return replace(counter, )

    #     return ""


    # def part2(self):
    #     reverse_molecule = self.molecule[::-1]

    #     for i in range(len(reverse_molecule)):
    #         replacement = ""
    #         for key, value in self.mapping.items():




def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == 4 else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2015, 19, None, part2)


if __name__ == "__main__":
    main()
