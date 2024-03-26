import os
import re
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

        cur_data = self.data.copy()

        info = {}

        for i in range(len(cur_data)):
            for j in range(1, len(cur_data[i][1:])):
                key = cur_data[i][j][0:-2].strip()
                if key in info:
                    info[key].append(cur_data[i][j][-2:].strip())
                else:
                    info[key] = [cur_data[i][j][-2:].strip()]

        ingredients = [ingr for ingr in info.keys()]

        teaspoons = 100
        max_score = 0

        for i in range(teaspoons + 1):
            for j in range(teaspoons + 1 - i):
                for k in range(teaspoons + 1 - i - j):
                    l = teaspoons - i - j - k
                    score = 1
                    for ingredient in ingredients:
                        score *= max(
                            0,
                            int(info[ingredient][0]) * i
                            + int(info[ingredient][1]) * j
                            + int(info[ingredient][2]) * k
                            + int(info[ingredient][3]) * l,
                        )
                    max_score = max(max_score, score)

        return max_score

    def part2(self):
        cur_data = self.data.copy()

        info = {}

        for i in range(len(cur_data)):
            for j in range(1, len(cur_data[i])):
                key = cur_data[i][j][0:-2].strip()
                if key in info:
                    info[key].append(cur_data[i][j][-2:].strip())
                else:
                    info[key] = [cur_data[i][j][-2:].strip()]

        ingredients = [ingr for ingr in info.keys()]

        teaspoons = 100
        max_score = 0

        for i in range(teaspoons + 1):
            for j in range(teaspoons + 1 - i):
                for k in range(teaspoons + 1 - i - j):
                    l = teaspoons - i - j - k

                    if (
                        i * int(info["calories"][0])
                        + j * int(info["calories"][1])
                        + k * int(info["calories"][2])
                        + l * int(info["calories"][3])
                        == 500
                    ):
                        score = 1
                        for ingredient in ingredients[:-1]:
                            score *= max(
                                0,
                                int(info[ingredient][0]) * i
                                + int(info[ingredient][1]) * j
                                + int(info[ingredient][2]) * k
                                + int(info[ingredient][3]) * l,
                            )

                        max_score = max(max_score, score)

        return max_score


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
    request_submit(2015, 15, part1, part2)


if __name__ == "__main__":
    main()
