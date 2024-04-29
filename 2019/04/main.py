import sys
import time

sys.path.insert(0, "../../")


def parseLine(line):
    return line


class Solution:
    def __init__(self, test=False):
        self.test = test
        filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(filename).read().rstrip()

    def check_criteria(self, password):
        password = [int(d) for d in str(password)]

        if all(i <= j for i, j in zip(password, password[1:])) and any(
            c1 == c2 for c1, c2 in zip(password, password[1:])
        ):
            return True

        return False

    def part1(self):
        minimum, maximum = map(int, self.data.split("-"))
        valid_passwords = set()

        for i in range(minimum, maximum + 1):
            if self.check_criteria(i):
                valid_passwords.add(i)

        return len(valid_passwords)

    def check_criteria_2(self, password):
        password = [int(d) for d in str(password)]

        if all(i <= j for i, j in zip(password, password[1:])) and 2 in [
            password.count(d) for d in password
        ]:
            return True

        return False

    def part2(self):
        minimum, maximum = map(int, self.data.split("-"))
        valid_passwords = set()

        for i in range(minimum, maximum + 1):
            if self.check_criteria_2(i):
                valid_passwords.add(i)

        return len(valid_passwords)


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
