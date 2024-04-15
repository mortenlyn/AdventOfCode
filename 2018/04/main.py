import re
import sys
import time
from collections import defaultdict, deque
from pprint import pprint

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
        self.sorted_data = self.data.copy()

        for i in range(len(self.sorted_data)):
            removed_brackets = (
                "".join(self.sorted_data[i]).replace("[", "").replace("]", "")
            )
            self.sorted_data[i] = re.split(r"[|]|:|-| ", removed_brackets)

        self.sorted_data.sort(key=lambda x: int("".join(x[:5])))
        self.guard_info = {}

        fell_asleep = 0
        current_guard = None

        for line in self.sorted_data:
            number = "".join(re.findall(r"#\d+", " ".join(line)))[1:]

            if number:
                current_guard = number
                if current_guard not in self.guard_info:
                    self.guard_info[current_guard] = {}

            if " ".join(line[-2:]) == "falls asleep":
                fell_asleep = int(line[4])

            elif " ".join(line[-2:]) == "wakes up":
                woke_up = int(line[4])

                for i in range(fell_asleep, woke_up):
                    if i in self.guard_info[current_guard]:
                        self.guard_info[current_guard][i] += 1
                    else:
                        self.guard_info[current_guard][i] = 1

    def part1(self):
        most_sleep = (None, 0)

        for guard, info in self.guard_info.items():
            total_sleep = sum(info.values())
            if total_sleep > most_sleep[-1]:
                most_sleep = (guard, total_sleep)

        max_key = max(
            self.guard_info[most_sleep[0]], key=self.guard_info[most_sleep[0]].get
        )

        return max_key * int(most_sleep[0])

    def part2(self):
        most_sleep = (None, 0, 0)

        for guard, info in self.guard_info.items():
            if info:
                max_key = max(info, key=info.get)
                if most_sleep[1] == 0:
                    most_sleep = (guard, max_key, info[max_key])

                elif info[max_key] > most_sleep[-1]:
                    most_sleep = (guard, max_key, info[max_key])

        return int(most_sleep[0]) * int(most_sleep[1])


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
