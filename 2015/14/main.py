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
        info = {}
        for line in self.data:
            line = line.split()
            name = line[0]
            speed = int(line[3])
            fly_time = int(line[6])
            rest_time = int(line[-2])

            info[name] = (speed, fly_time, rest_time)

        max_distance = 0

        for reindeer in info:
            seconds = 2503
            speed, fly_time, rest_time = info[reindeer]
            distance = 0
            while seconds > 0:
                distance += speed * min(fly_time, seconds)
                seconds -= fly_time
                seconds -= rest_time

            max_distance = max(max_distance, distance)

        return max_distance

    def part2(self):
        info = {}
        for line in self.data:
            line = line.split()
            name = line[0]
            speed = int(line[3])
            fly_time = int(line[6])
            rest_time = int(line[-2])

            info[name] = (speed, fly_time, rest_time)

        points = {reindeer: 0 for reindeer in info}
        current_distances = {reindeer: 0 for reindeer in info}
        current_max_distance = 0

        for i in range(0, 2504):
            for reindeer in info:
                speed, fly_time, rest_time = info[reindeer]
                current_distances[reindeer] += (
                    speed if i % (fly_time + rest_time) < fly_time else 0
                )
                current_max_distance = max(
                    current_max_distance, current_distances[reindeer]
                )

            for reindeer in info:
                if current_distances[reindeer] == current_max_distance:
                    points[reindeer] += 1

        return max(points.values())


def main():
    start = time.perf_counter()

    # test = Solution(test=True)
    # test1 = test.part1()
    # test2 = test.part2()
    # print(f"(TEST) Part 1: {test1}, \t{'correct :)' if test1 == None else 'wrong :('}")
    # print(f"(TEST) Part 2: {test2}, \t{'correct :)' if test2 == None else 'wrong :('}")

    solution = Solution()
    part1 = solution.part1()
    part2 = solution.part2()
    print(part1_text := f"Part 1: {part1}")
    print(part2_text := f"Part 2: {part2}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")

    copy_answer(part1, part2)
    write_solution(os.path.dirname(os.path.realpath(__file__)), part1_text, part2_text)
    request_submit(2015, 14, part1, part2)


if __name__ == "__main__":
    main()
