import os
import re
import time

import networkx
from aoc_utils_runarmod import copy_answer, get_data, request_submit, write_solution


def parseLine(line):
    return line


def parseLines(lines):
    return [parseLine(line) for line in lines]


def nums(line: str) -> tuple[int, ...]:
    return tuple(map(int, re.findall(r"-?\d+", line)))


def numsNested(
    data: str | list[str] | list[list[str]],
) -> list[int | tuple[int, ...], ...]:
    if isinstance(data, str):
        return nums(data)
    if not hasattr(data, "__iter__"):
        raise ValueError("Data must be a tuple/list/iterable or a string")
    return list(e[0] if len(e) == 1 else e for e in filter(len, map(numsNested, data)))


class Solution:
    def __init__(self, test=False):
        self.test = test
        data = get_data(2024, 5, test=test).strip("\n").split("\n")
        rules = []
        updates = []
        for i in range(len(data)):
            if data[i] == "":
                rules = data[:i]
                updates = data[i+1::]
                break

        self.rules = numsNested(rules)
        self.updates = numsNested(updates)

        self.rule_dict = {}

        for elem in self.rules:
            if elem[1] in self.rule_dict:
                self.rule_dict[elem[1]].append(elem[0])
            else:
                self.rule_dict[elem[1]] = [elem[0]]

    def make_graph(self, update):
        graph = networkx.DiGraph()

        for key in update:
            for value in self.rule_dict.get(key, []):
                graph.add_edge(key, value)

        return graph

    def top_sort(self, graph):
        return networkx.topological_sort(graph)

    def check_if_valid(self, update):
        for i in range(len(update)):
            for elem in update[i+1::]:
                if update[i] in self.rule_dict and elem in self.rule_dict[update[i]]:
                    return False
        return True

    def fix_update(self, update):
        return list(filter(lambda elem: elem in update,self.top_sort(self.make_graph(update))))

    def part1(self):
        all_valid = [elem for elem in self.updates if self.check_if_valid(elem)]
        return sum(elem[len(elem)//2] for elem in all_valid)

    def part2(self):
        all_invalid = [elem for elem in self.updates if not self.check_if_valid(elem)]
        corrected_updates = [self.fix_update(elem) for elem in all_invalid]

        return sum(elem[len(elem)//2] for elem in corrected_updates)


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
