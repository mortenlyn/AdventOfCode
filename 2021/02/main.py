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

    def add_to_position(self, instruction, length, depth, horizontal_pos):
        match instruction:
            case "forward":
                horizontal_pos += int(length)
            case "down":
                depth += int(length)
            case "up":
                depth -= int(length)

        return depth, horizontal_pos

    def part1(self):
        depth = 0
        horizontal_pos = 0

        for instruction in self.data:
            inst, length = instruction.split(" ")

            depth, horizontal_pos = self.add_to_position(
                inst, length, depth, horizontal_pos
            )

        return depth * horizontal_pos

    def add_to_position_with_aim(self, instruction, length, depth, horizontal_pos, aim):
        match instruction:
            case "forward":
                horizontal_pos += int(length)
                depth += int(aim) * int(length)
            case "down":
                aim += int(length)
            case "up":
                aim -= int(length)

        return depth, horizontal_pos, aim

    def part2(self):
        depth = 0
        horizontal_pos = 0
        aim = 0

        for instruction in self.data:
            inst, length = instruction.split(" ")

            depth, horizontal_pos, aim = self.add_to_position_with_aim(
                inst, length, depth, horizontal_pos, aim
            )

        return depth * horizontal_pos


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
    request_submit(2021, 2, part1, part2)


if __name__ == "__main__":
    main()
