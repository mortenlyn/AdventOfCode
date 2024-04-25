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
        self.data = [
            parseLine(line) for line in open(filename).read().rstrip().split("\n")
        ]

        self.coords = [tuple(map(int, line.split(", "))) for line in self.data]
        self.min_x = min(x for x, y in self.coords)
        self.max_x = max(x for x, y in self.coords)
        self.min_y = min(y for x, y in self.coords)
        self.max_y = max(y for x, y in self.coords)

        self.grid = {}
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                distances = sorted(
                    (
                        (self.manhattenDistance(x, y, cx, cy), i)
                        for i, (cx, cy) in enumerate(self.coords)
                    )
                )
                self.grid[x, y] = distances[0][1]

        self.infinite = set()

        for x in range(self.min_x, self.max_x + 1):
            self.infinite.add(self.grid[x, self.min_y])
            self.infinite.add(self.grid[x, self.max_y])

        for y in range(self.min_y, self.max_y + 1):
            self.infinite.add(self.grid[self.min_x, y])
            self.infinite.add(self.grid[self.max_x, y])

        self.areas = defaultdict(int)

        for coord in self.grid.values():
            if coord not in self.infinite:
                self.areas[coord] += 1

    def manhattenDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def part1(self):
        return max(self.areas.values())

    def part2(self):
        max_range = 10000
        region_area = 0

        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                if (
                    sum(self.manhattenDistance(x, y, cx, cy) for cx, cy in self.coords)
                    < max_range
                ):
                    region_area += 1

        return region_area


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
