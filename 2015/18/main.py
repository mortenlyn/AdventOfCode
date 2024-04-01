import itertools
import sys
import time
from collections import Counter, defaultdict, deque
from pprint import pprint

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            parseLine(line) for line in open(filename).read().rstrip().split("\n")
        ]

    def decide_next_state(self, data, i, j):
        num_rows = len(data)
        num_cols = len(data[0])

        neighbors = sum(
            1
            for x in range(max(0, i - 1), min(num_rows, i + 2))
            for y in range(max(0, j - 1), min(num_cols, j + 2))
            if data[x][y] == "#"
        )

        if data[i][j] == "#":
            neighbors -= 1
            return "#" if neighbors in [2, 3] else "."
        else:
            return "#" if neighbors == 3 else "."

    def part1(self):
        result = self.data.copy()
        temp = []

        for _ in range(100):
            for i in range(len(result)):
                row = ""
                for j in range(len(result[0])):
                    row += self.decide_next_state(result, i, j)
                temp.append(row)
            result = temp.copy()
            temp.clear()

        return Counter(itertools.chain(*result))["#"]

    def next_state_corners_on(self, data, i, j):
        if (i, j) in [
            (0, 0),
            (0, len(data[0]) - 1),
            (len(data) - 1, 0),
            (len(data) - 1, len(data[0]) - 1),
        ]:
            return "#"

        num_rows = len(data)
        num_cols = len(data[0])

        neighbors = sum(
            1
            for x in range(max(0, i - 1), min(num_rows, i + 2))
            for y in range(max(0, j - 1), min(num_cols, j + 2))
            if data[x][y] == "#"
        )

        if data[i][j] == "#":
            neighbors -= 1
            return "#" if neighbors in [2, 3] else "."
        else:
            return "#" if neighbors == 3 else "."

    def part2(self):
        result = self.data.copy()
        temp = []

        for _ in range(100):
            for i in range(len(result)):
                row = ""
                for j in range(len(result[0])):
                    row += self.next_state_corners_on(result, i, j)
                temp.append(row)
            result = temp.copy()
            temp.clear()

        return Counter(itertools.chain(*result))["#"]


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
