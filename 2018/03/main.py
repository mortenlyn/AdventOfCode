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

        self.fabric = []

        self.max_x = max(
            [
                int(line.split()[2].split(",")[0]) + int(line.split()[-1].split("x")[0])
                for line in self.data
            ]
        )

        self.max_y = max(
            [
                int(line.split()[2].split(",")[1].strip(":"))
                + int(line.split()[-1].split("x")[1])
                for line in self.data
            ]
        )

        for _ in range(self.max_x):
            self.fabric.append([0] * self.max_y)

        for line in self.data:
            x = int(line.split()[2].split(",")[0])
            y = int(line.split()[2].split(",")[1].strip(":"))
            width = int(line.split()[-1].split("x")[0])
            height = int(line.split()[-1].split("x")[1])
            for i in range(x, x + width):
                for j in range(y, y + height):
                    self.fabric[i][j] += 1

    def part1(self):
        count = 0

        for i in range(self.max_x):
            for j in range(self.max_y):
                if self.fabric[i][j] > 1:
                    count += 1

        return count

    def part2(self):
        for line in self.data:
            x = int(line.split()[2].split(",")[0])
            y = int(line.split()[2].split(",")[1].strip(":"))
            width = int(line.split()[-1].split("x")[0])
            height = int(line.split()[-1].split("x")[1])

            overlap = False

            for i in range(x, x + width):
                for j in range(y, y + height):
                    if self.fabric[i][j] > 1:
                        overlap = True
                        break

                if overlap:
                    break

            if not overlap:
                return line.split()[0][1:]


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
