import sys
import time

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(line) for line in open(filename).read().rstrip().split("\n")]

    def part1(self):
        result = 0

        for i in range(len(self.data) - 1):
            if self.data[i + 1] > self.data[i]:
                result += 1

        return result

    def part2(self):
        result = 0

        for i in range(2, len(self.data) - 1):
            if sum(self.data[i - 2 : i + 1]) < sum(self.data[i - 1 : i + 2]):
                result += 1

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
