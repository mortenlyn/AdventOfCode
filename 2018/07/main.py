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

        self.prereq_overview = defaultdict(list)
        for line in self.data:
            words = line.split()
            self.prereq_overview[words[7]].append(words[1])
            self.prereq_overview[words[1]]

    def part1(self):
        result = ""
        prereq_overview = defaultdict(list)

        for line in self.data:
            words = line.split()
            prereq_overview[words[7]].append(words[1])
            prereq_overview[words[1]]

        while prereq_overview:
            next_step = min(
                [step for step, prereqs in prereq_overview.items() if len(prereqs) == 0]
            )
            result += next_step
            del prereq_overview[next_step]
            for prereqs in prereq_overview.values():
                if next_step in prereqs:
                    prereqs.remove(next_step)

        return result

    def part2(self):
        prereq_overview = defaultdict(list)

        for line in self.data:
            words = line.split()
            prereq_overview[words[7]].append(words[1])
            prereq_overview[words[1]]

        workers = [(None, 0)] * 5
        time = 0
        completed_steps = set()

        while prereq_overview or any(worker[1] > 0 for worker in workers):
            for i, (step, remaining_time) in enumerate(workers):
                if remaining_time == 0:
                    ready_steps = [
                        step
                        for step, prereqs in prereq_overview.items()
                        if all(prereq in completed_steps for prereq in prereqs)
                    ]
                    if not ready_steps:
                        continue
                    next_step = min(ready_steps)
                    workers[i] = (
                        next_step,
                        ord(next_step) - 4,
                    )
                    del prereq_overview[next_step]

            for i, (step, remaining_time) in enumerate(workers):
                if remaining_time == 0:
                    ready_steps = [
                        step
                        for step, prereqs in prereq_overview.items()
                        if all(prereq in completed_steps for prereq in prereqs)
                    ]
                    if not ready_steps:
                        continue
                    next_step = min(ready_steps)
                    workers[i] = (
                        next_step,
                        ord(next_step) - 4,
                    )
                    del prereq_overview[next_step]
                else:
                    workers[i] = (
                        step,
                        remaining_time - 1,
                    )
                    if remaining_time == 1:
                        completed_steps.add(step)
            time += 1

        return time


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
