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

    def summable(self, number, lst):
        for i in range(len(lst)):
            lst_without_value = lst[:]
            lst_without_value.remove(lst[i])
            if number - lst[i] in lst_without_value:
                return True
        return False

    def part1(self):
        amount_of_numbers = 25
        numbers = list(map(int, self.data))

        for i in range(amount_of_numbers, len(numbers)):
            if not self.summable(numbers[i], numbers[(i - amount_of_numbers) : i]):
                return numbers[i]

    def part2(self):
        invalid_number = self.part1()
        numbers = list(map(int, self.data))

        for i in range(len(numbers)):
            current_numbers = [numbers[i]]
            for j in range(i + 1, len(numbers)):
                current_numbers.append(numbers[j])

                if sum(current_numbers) == invalid_number:
                    return min(current_numbers) + max(current_numbers)


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
    request_submit(2020, 9, part1, part2)


if __name__ == "__main__":
    main()
