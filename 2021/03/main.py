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

    def calculate_gamma(self, report):
        gamma_list = [0 for i in range(len(report[0]))]

        for bit_string in report:
            for i in range(len(bit_string)):
                if bit_string[i] == "1":
                    gamma_list[i] += 1
                else:
                    gamma_list[i] -= 1

        gamma = ""
        for i in range(len(gamma_list)):
            if gamma_list[i] >= 0:
                gamma += "1"
            else:
                gamma += "0"

        return gamma

    def calculate_epsilon(self, gamma):
        epsilon = ""
        for bit in gamma:
            if bit == "1":
                epsilon += "0"
            else:
                epsilon += "1"

        return epsilon

    def part1(self):
        gamma = self.calculate_gamma(self.data)
        epsilon = self.calculate_epsilon(gamma)

        return int(gamma, 2) * int(epsilon, 2)

    def determine_oxy_gen_rating(self, bit_criteria_nums, counter):
        if len(bit_criteria_nums) == 1:
            return "".join(bit_criteria_nums)
        if len(bit_criteria_nums) == 0:
            bit_criteria_nums = self.data.copy()

        bit_criteria_most_common = []
        gamma = self.calculate_gamma(bit_criteria_nums)

        for bit_string in bit_criteria_nums:
            if bit_string[counter] == gamma[counter]:
                bit_criteria_most_common.append(bit_string)

        counter += 1

        return self.determine_oxy_gen_rating(bit_criteria_most_common, counter)

    def determine_CO2_scr_rating(self, bit_criteria_nums, counter):
        if len(bit_criteria_nums) == 1:
            return "".join(bit_criteria_nums)

        if len(bit_criteria_nums) == 0:
            bit_criteria_nums = self.data.copy()

        bit_criteria_least_common = []
        gamma = self.calculate_gamma(bit_criteria_nums)
        epsilon = self.calculate_epsilon(gamma)

        for bit_string in bit_criteria_nums:
            if bit_string[counter] == epsilon[counter]:
                bit_criteria_least_common.append(bit_string)

        counter += 1

        return self.determine_CO2_scr_rating(bit_criteria_least_common, counter)

    def part2(self):
        oxy_gen_rating = self.determine_oxy_gen_rating([], 0)
        CO2_scr_rating = self.determine_CO2_scr_rating([], 0)

        return int(oxy_gen_rating, 2) * int(CO2_scr_rating, 2)


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
    request_submit(2021, 3, None, part2)


if __name__ == "__main__":
    main()
