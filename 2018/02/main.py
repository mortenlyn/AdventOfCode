import itertools
import sys
import time

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

    def part1(self):
        double = 0
        triple = 0

        for line in self.data:
            letters = set()
            d = False
            t = False
            for letter in line:
                if letter in letters:
                    continue

                letters.add(letter)

                if line.count(letter) == 2 and not d:
                    double += 1
                    d = True

                if line.count(letter) == 3 and not t:
                    triple += 1
                    t = True

        return double * triple

    def part2(self):
        for a, b in itertools.combinations(self.data, 2):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return "".join([a[i] for i in range(len(a)) if a[i] == b[i]])


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
