def check(registers, register, operator, num):
    return {
        ">": lambda a, b: a > b,
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
        ">=": lambda a, b: a >= b,
        "!=": lambda a, b: a != b,
        "==": lambda a, b: a == b,
    }[operator](registers[register], num)


def update(instruction, num):
    if instruction == "inc":
        return num
    return -num


def part1():
    data = open("input.txt").read().strip().split("\n")

    registers = {}

    data = [line.split(" ") for line in data]

    for line in data:
        if line[0] not in registers:
            registers[line[0]] = 0

        if line[-3] not in registers:
            registers[line[-3]] = 0

        if not check(registers, line[-3], line[-2], int(line[-1])):
            continue

        registers[line[0]] += update(line[1], int(line[2]))

    return (max(registers.values()))


print("Part 1:", part1())


def part2():
    data = open("input.txt").read().strip().split("\n")

    registers = {}

    data = [line.split(" ") for line in data]

    maximum = 0

    for line in data:
        if line[0] not in registers:
            registers[line[0]] = 0

        if line[-3] not in registers:
            registers[line[-3]] = 0

        if not check(registers, line[-3], line[-2], int(line[-1])):
            continue

        registers[line[0]] += update(line[1], int(line[2]))

        if registers[line[0]] > maximum:
            maximum = registers[line[0]]

    return (maximum)


print("Part 2:", part2())
