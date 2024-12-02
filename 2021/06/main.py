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
            parseLine(int(line)) for line in open(filename).read().rstrip().split(",")
        ]

    def check_status(self, fish_counts):
        new_fish_counts = {i: 0 for i in range(9)}

        for timer, count in fish_counts.items():
            if timer == 0:
                new_fish_counts[8] += count
                new_fish_counts[6] += count
            else:
                new_fish_counts[timer - 1] += count

        return new_fish_counts

    def fish_simulator(self, total_days):
        fish_counts = {i: 0 for i in range(9)}
        for timer in self.data:
            fish_counts[timer] += 1

        for _ in range(total_days):
            fish_counts = self.check_status(fish_counts)

        return sum(fish_counts.values())

    def part1(self):
        return self.fish_simulator(80)

    def part2(self):
        return self.fish_simulator(256)


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
