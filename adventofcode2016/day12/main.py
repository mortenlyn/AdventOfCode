def cpy(line, registers):
    if line[1].isdigit():
        num = int(line[1])
        registers[line[-1]] = num
    else:
        num = registers[line[1]]
        registers[line[-1]] = num

    return registers


def inc(line, registers):
    registers[line[-1]] += 1

    return registers


def dec(line, registers):
    registers[line[-1]] -= 1

    return registers


def part1():
    data = open("adventofcode2016\day12\input.txt").read().strip().split("\n")

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}

    for i in range(len(data)):
        data[i] = data[i].split()

    i = 0

    while i < len(data):
        if data[i][0] == "cpy":
            registers = cpy(data[i], registers)
            i += 1
        elif data[i][0] == "inc":
            registers = inc(data[i], registers)
            i += 1
        elif data[i][0] == "dec":
            registers = dec(data[i], registers)
            i += 1
        elif data[i][0] == "jnz":
            if data[i][1].isdigit():
                if int(data[i][1]) == 0:
                    i += 1
                else:
                    i += int(data[i][-1])

            else:
                if registers[data[i][1]] == 0:
                    i += 1
                else:
                    i += int(data[i][-1])

    print(registers["a"])


part1()


def part2():
    data = open("adventofcode2016\day12\input.txt").read().strip().split("\n")

    registers = {"a": 0, "b": 0, "c": 1, "d": 0}

    for i in range(len(data)):
        data[i] = data[i].split()

    i = 0

    while i < len(data):
        if data[i][0] == "cpy":
            registers = cpy(data[i], registers)
            i += 1
        elif data[i][0] == "inc":
            registers = inc(data[i], registers)
            i += 1
        elif data[i][0] == "dec":
            registers = dec(data[i], registers)
            i += 1
        elif data[i][0] == "jnz":
            if data[i][1].isdigit():
                if int(data[i][1]) == 0:
                    i += 1
                else:
                    i += int(data[i][-1])
            else:
                if registers[data[i][1]] == 0:
                    i += 1
                else:
                    i += int(data[i][-1])
    print(registers["a"])


part2()
