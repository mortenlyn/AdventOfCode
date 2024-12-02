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
        self.data = [
            parseLine(line) for line in open(filename).read().rstrip().split("\n")
        ]
        self.info = [elem.split(" ") for elem in self.data]

    def valid(self, elem):
        elem = list(map(int, elem))
        if sorted(elem) != elem and sorted(elem, reverse=True) != elem:
            return False
        for i in range(len(elem) - 1):
            diff = abs(elem[i + 1] - elem[i])
            if diff > 3 or diff < 1:
                return False

        return True

    def part1(self):
        return sum(map(self.valid, self.info))

    def part2(self):
        safe = 0

        for elem in self.info:
            elem = list(map(int, elem))

            if self.valid(elem):
                safe += 1
                continue

            for i in range(len(elem)):
                removed = elem.pop(i)
                if self.valid(elem):
                    safe += 1
                    break
                elem.insert(i, removed)

        return safe


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
