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

    def check_visible(self, line, index):
        tree_height = self.data[line][index]
        over = True
        under = True
        right = True
        left = True

        for i in range(line):
            if self.data[i][index] >= tree_height:
                over = False
                break

        for i in range(line + 1, len(self.data)):
            if self.data[i][index] >= tree_height:
                under = False
                break

        for i in range(index):
            if self.data[line][i] >= tree_height:
                left = False
                break

        for i in range(index + 1, len(self.data[0])):
            if self.data[line][i] >= tree_height:
                right = False
                break

        if over or under or right or left:
            return 1

        return 0

    def part1(self):
        visible = 2 * (len(self.data) - 2) + (2 * len(self.data[0]))

        for i in range(1, len(self.data) - 1):
            for j in range(1, len(self.data[i]) - 1):
                visible += self.check_visible(i, j)

        return visible

    def scenic_score(self, line, index):
        tree_height = self.data[line][index]
        over = 0
        under = 0
        right = 0
        left = 0

        for i in range(line - 1, -1, -1):
            over += 1
            if self.data[i][index] >= tree_height:
                break

        for i in range(line + 1, len(self.data)):
            under += 1
            if self.data[i][index] >= tree_height:
                break

        for i in range(index - 1, -1, -1):
            left += 1
            if self.data[line][i] >= tree_height:
                break

        for i in range(index + 1, len(self.data[0])):
            right += 1
            if self.data[line][i] >= tree_height:
                break

        return right * left * over * under

    def part2(self):
        score = 0

        for i in range(1, len(self.data) - 1):
            for j in range(1, len(self.data[i]) - 1):
                score = max(score, self.scenic_score(i, j))

        return score


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
