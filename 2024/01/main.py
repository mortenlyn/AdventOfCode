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
        self.info = [elem.split("   ") for elem in self.data]

    def part1(self):
        ls = []
        rs = []

        for elem in self.info:
            ls.append(elem[0])
            rs.append(elem[1])

        ls = list(map(int, ls))
        rs = list(map(int, rs))

        ls = sorted(ls)
        rs = sorted(rs)

        return sum(abs(ls[i] - rs[i]) for i in range(len(ls)))

    def part2(self):
        ls = []
        rs = []

        for elem in self.info:
            ls.append(elem[0])
            rs.append(elem[1])

        ls = list(map(int, ls))
        rs = list(map(int, rs))

        ls = sorted(ls)
        rs = sorted(rs)

        result = 0

        for i in range(len(ls)):
            k = ls[i]
            count = sum(1 for elem in rs if elem == k)
            result += k * count

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
