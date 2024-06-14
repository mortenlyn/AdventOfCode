import sys
import time
from collections import defaultdict

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [int(line) for line in open(filename).read().rstrip().split("\n")]

    def part1(self):
        adapters = sorted(self.data)
        adapters.append(adapters[-1] + 3)
        jolt_differences = defaultdict(int)
        current_voltage = 0

        for adapter in adapters:
            differance = adapter - current_voltage
            if differance < 4:
                jolt_differences[differance] += 1

            current_voltage = adapter

        return jolt_differences[1] * jolt_differences[3]

    def count_combinations(self, adapters):
        combinations_count = [0] * len(adapters)
        combinations_count[0] = 1

        for i in range(1, len(adapters)):
            for j in range(i):
                if adapters[i] - adapters[j] <= 3:
                    combinations_count[i] += combinations_count[j]

        return combinations_count[-1]

    def part2(self):
        adapters = sorted(self.data)
        adapters.insert(0, 0)
        adapters.append(adapters[-1] + 3)

        return self.count_combinations(adapters)


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
