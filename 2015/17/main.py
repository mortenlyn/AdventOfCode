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
        container_sizes = sorted(list(map(int, self.data)))

        def find_combinations(numbers, target):
            if target == 0:
                return 1
            if not numbers or target < 0:
                return 0
            return find_combinations(numbers[1:], target) + find_combinations(
                numbers[1:], target - numbers[0]
            )

        return find_combinations(container_sizes, 150)

    def part2(self):
        container_sizes = sorted(list(map(int, self.data)))

        def find_min_subset(num_of_containers, target_capacity):
            smallest_subset_size = target_capacity
            for index, container_size in enumerate(container_sizes[:num_of_containers]):
                if container_size <= target_capacity:
                    subset_size = (
                        find_min_subset(index, target_capacity - container_size) + 1
                    )
                    if subset_size < smallest_subset_size:
                        smallest_subset_size = subset_size
            return smallest_subset_size

        return find_min_subset(len(container_sizes), 150)


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
