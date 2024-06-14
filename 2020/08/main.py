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

    def execute_instruction(self, instruction, value, accumulator, i):
        match instruction:
            case "nop":
                return accumulator, i + 1
            case "acc":
                return accumulator + int(value), i + 1
            case "jmp":
                return accumulator, i + int(value)

    def part1(self):
        accumulator = 0
        instruction_index = set()
        i = 0

        while i < len(self.data):
            if i in instruction_index:
                return accumulator
            instruction_index.add(i)

            instruction, value = self.data[i].split(" ")

            accumulator, i = self.execute_instruction(
                instruction, value, accumulator, i
            )

    def check_terminates(self, instructions):
        threshold = 10000
        loops = 0
        accumulator = 0
        i = 0

        while i < len(instructions):
            instruction, value = instructions[i].split(" ")

            accumulator, i = self.execute_instruction(
                instruction, value, accumulator, i
            )

            loops += 1

            if loops > threshold:
                return False, accumulator

        return True, accumulator

    def change_instruction(self, instructions, i, instruction, value):
        new_instructions = instructions.copy()
        if instruction == "nop":
            new_instructions[i] = "jmp" + " " + value
        else:
            new_instructions[i] = "nop" + " " + value

        return self.check_terminates(new_instructions)

    def part2(self):
        instructions = self.data.copy()
        i = 0

        while i < len(instructions):
            instruction, value = self.data[i].split(" ")
            if instruction == "nop":
                check, accumulator = self.change_instruction(
                    instructions, i, instruction, value
                )
                if check:
                    return accumulator

            elif instruction == "jmp":
                check, accumulator = self.change_instruction(
                    instructions, i, instruction, value
                )
                if check:
                    return accumulator

            i += 1

        return None


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
