import re
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

    def supportsTLS(self, sequence):
        reverse_pair = re.findall(r"([a-zA-Z])([a-zA-Z])\2\1", sequence)
        for pair in reverse_pair:
            if pair[0] == pair[1]:
                return False
        if reverse_pair:
            return True

    def part1(self):
        result = 0

        sequences = [re.split(r"\[|\]", line) for line in self.data]

        for line in sequences:
            supports_TLS = False

            for i, sequence in enumerate(line):
                if i % 2 == 1:
                    if self.supportsTLS(sequence):
                        supports_TLS = False
                        break
                if i % 2 == 0:
                    if self.supportsTLS(sequence):
                        supports_TLS = True

            if supports_TLS:
                result += 1

        return result

    def findABA(self, sequence):
        aba = re.findall(r"(?=([a-zA-Z])([a-zA-Z])(\1))", sequence)

        if not aba:
            return []

        result = []

        for pair in aba:
            if pair[0] != pair[1]:
                result.append(pair)

        return result

    def findBAB(self, sequence, aba):
        bab = re.findall(r"(?=([a-zA-Z])([a-zA-Z])(\1))", sequence)
        wanted = aba[1] + aba[0] + aba[1]
        for pair in bab:
            if "".join(pair) == wanted:
                return True
        return False

    def part2(self):
        result = 0
        IP_addresses = []

        sequences = [re.split(r"\[|\]", line) for line in self.data]
        for line in sequences:
            aba = []
            for i, sequence in enumerate(line):
                if i % 2 == 0:
                    for a in self.findABA(sequence):
                        aba.append(a)

            for i, sequence in enumerate(line):
                if i % 2 == 1:
                    for a in aba:
                        if self.findBAB(sequence, a):
                            result += 1
                            IP_addresses.append(line)
                            break

        return result


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
