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

    def supportsTLS(self, sequence):
        reverse_pair = re.findall(r"([a-zA-Z])([a-zA-Z])\2\1", sequence)
        for pair in reverse_pair:
            if pair[0] == pair[1]:
                return False
        if reverse_pair:
            return True

    def part1(self):
        result = 0

        sequences = [re.split(r"\[|\]", line) for line in self.data]

        for line in sequences:
            supports_TLS = False

            for i, sequence in enumerate(line):
                if i % 2 == 1:
                    if self.supportsTLS(sequence):
                        supports_TLS = False
                        break
                if i % 2 == 0:
                    if self.supportsTLS(sequence):
                        supports_TLS = True

            if supports_TLS:
                result += 1

        return result

    def findABA(self, sequence):
        aba = re.findall(r"(?=([a-zA-Z])([a-zA-Z])(\1))", sequence)

        if not aba:
            return []

        for pair in aba:
            if pair[0] == pair[1]:
                return []

        return aba

    def findBAB(self, sequence, aba):
        bab = re.findall(r"(?=([a-zA-Z])([a-zA-Z])(\1))", sequence)
        wanted = aba[1] + aba[0] + aba[1]
        for pair in bab:
            if "".join(pair) == wanted:
                return True
        return False

    def part2(self):
        result = 0

        sequences = [re.split(r"\[|\]", line) for line in self.data]

        for line in sequences:
            aba = []
            for i, sequence in enumerate(line):
                if i % 2 == 0:
                    for a in self.findABA(sequence):
                        aba.append(a)

            for i, sequence in enumerate(line):
                if i % 2 == 1:
                    for a in aba:
                        if self.findBAB(sequence, a):
                            result += 1
        return result


def main():
    start = time.perf_counter()

    test = Solution(test=True)
    test1 = test.part1()
    test2 = test.part2()
    print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2016, 7, part1, part2)


if __name__ == "__main__":
    main()
