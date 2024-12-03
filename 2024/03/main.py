import functools
from operator import mul
import re
import sys
import time

sys.path.insert(0, "../../")
from utils import copy_answer, request_submit, write_solution


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(filename).read().rstrip()

    def part1(self):
        instructions = re.findall(r"mul\(\d+,\d+\)", self.data)

        result = 0

        for elem in instructions:
            nums = re.findall(r"\d+", elem)
            nums = map(int, nums)
            result += functools.reduce(mul, nums)

        return result

    def part2(self):
        instructions = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", self.data)

        result = 0
        do = True

        for elem in instructions:
            if elem == "don't()":
                do = False
            elif elem == "do()":
                do = True
            elif do:
                nums = re.findall(r"\d+", elem)
                nums = map(int, nums)
                result += functools.reduce(mul, nums)

        return result


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
