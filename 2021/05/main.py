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

        self.max_x = 0
        self.max_y = 0

        for line in self.data:
            vent_coords_start = line.split(" -> ")[0]
            x_start, y_start = vent_coords_start.split(",")
            vent_coords_end = line.split(" -> ")[1]
            x_end, y_end = vent_coords_end.split(",")

            self.max_x = max(self.max_x, int(x_start), int(x_end))
            self.max_y = max(self.max_y, int(y_start), int(y_end))

    def create_ocean_floor(self):
        ocean_floor = []

        for _ in range(self.max_y + 1):
            ocean_floor.append([0] * (self.max_x + 1))

        return ocean_floor

    def part1(self):
        ocean_floor = self.create_ocean_floor()

        for line in self.data:
            vent_coords_start = line.split(" -> ")[0]
            x_start, y_start = vent_coords_start.split(",")
            vent_coords_end = line.split(" -> ")[1]
            x_end, y_end = vent_coords_end.split(",")

            if x_start == x_end:
                for y in range(
                    min(int(y_start), int(y_end)), max(int(y_start), int(y_end)) + 1
                ):
                    ocean_floor[y][int(x_start)] += 1

            elif y_start == y_end:
                for x in range(
                    min(int(x_start), int(x_end)), max(int(x_start), int(x_end)) + 1
                ):
                    ocean_floor[int(y_start)][x] += 1

        count = 0
        for x in range(self.max_y + 1):
            for y in range(self.max_x + 1):
                if ocean_floor[x][y] >= 2:
                    count += 1

        return count

    def part2(self):
        ocean_floor = self.create_ocean_floor()

        for line in self.data:
            vent_coords_start = line.split(" -> ")[0]
            x_start, y_start = vent_coords_start.split(",")
            vent_coords_end = line.split(" -> ")[1]
            x_end, y_end = vent_coords_end.split(",")

            if x_start == x_end:
                for y in range(
                    min(int(y_start), int(y_end)), max(int(y_start), int(y_end)) + 1
                ):
                    ocean_floor[y][int(x_start)] += 1

            elif y_start == y_end:
                for x in range(
                    min(int(x_start), int(x_end)), max(int(x_start), int(x_end)) + 1
                ):
                    ocean_floor[int(y_start)][x] += 1
            else:
                slope = (int(y_end) - int(y_start)) / (int(x_end) - int(x_start))
                intercept = int(y_start) - slope * int(x_start)

                for x in range(
                    min(int(x_start), int(x_end)), max(int(x_start), int(x_end)) + 1
                ):
                    y = slope * x + intercept
                    ocean_floor[int(y)][x] += 1

        count = 0
        for x in range(self.max_y + 1):
            for y in range(self.max_x + 1):
                if ocean_floor[x][y] >= 2:
                    count += 1

        return count


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
