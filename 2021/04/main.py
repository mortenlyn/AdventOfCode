import re
import numpy as np
import sys
import time

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = [line for line in open(filename).read().rstrip().split("\n\n")]

    def simulate_pick_number(self, boards, nums, picked_nums):
        if len(picked_nums) > 4:
            for board in boards:
                for row in board:
                    row_nums = re.findall(r"\d+", row)
                    if set(row_nums).issubset(set(picked_nums)):
                        score = 0
                        for row in board:
                            row_nums = re.findall(r"\d+", row)
                            for num in row_nums:
                                if num not in picked_nums:
                                    score += int(num)

                        score *= int(picked_nums[-1])
                        return score

        if len(nums) == 0:
            return

        picked_nums.append(nums.pop(0))

        return self.simulate_pick_number(boards, nums, picked_nums)

    def part1(self):
        random_nums = self.data[0].split(",")
        bingo_boards = []

        for board in self.data[1:]:
            bingo_boards.append(board.strip().split("\n"))

        return self.simulate_pick_number(bingo_boards, random_nums, [])

    def simulate_pick_number_win_last(
        self, boards, nums, picked_nums, winning_boards, target_length
    ):
        updated_boards = boards.copy()

        if len(picked_nums) > 4:
            for board in boards:
                for row in board:
                    row_nums = re.findall(r"\d+", row)
                    if set(row_nums).issubset(set(picked_nums)):
                        winning_boards.append(board)
                        updated_boards.remove(board)
                        break

                if board in winning_boards:
                    continue

                transposed_board = np.transpose(
                    [re.findall(r"\d+", row) for row in board]
                )
                for row in transposed_board:
                    if set(row).issubset(set(picked_nums)):
                        winning_boards.append(board)
                        updated_boards.remove(board)
                        break

        if len(winning_boards) == target_length:
            score = 0
            for row in winning_boards[-1]:
                row_nums = re.findall(r"\d+", row)
                for num in row_nums:
                    if num not in picked_nums:
                        score += int(num)

            score *= int(picked_nums[-1])
            return score

        if len(nums) == 0:
            return

        picked_nums.append(nums.pop(0))

        return self.simulate_pick_number_win_last(
            updated_boards, nums, picked_nums, winning_boards, target_length
        )

    def part2(self):
        random_nums = self.data[0].split(",")
        bingo_boards = []

        for board in self.data[1:]:
            bingo_boards.append(board.strip().split("\n"))

        return self.simulate_pick_number_win_last(
            bingo_boards, random_nums, [], [], len(bingo_boards)
        )


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
