import time


def extend_line(line):
    if all(i == line[0] for i in line):
        return line + [line[-1]]

    difference_list = []

    for i in range((len(line)-1)):
        difference_list.append(line[i+1] - line[i])

    next_line = extend_line(difference_list)

    return line + [next_line[-1] + line[-1]]


def part1():
    data = open("adventofcode2023\day9\input.txt",
                "r").read().strip().split("\n")
    result = 0

    for line in range(len(data)):
        line_result = data[line].split()
        line_result = list(map(int, line_result))

        line_result = extend_line(line_result)

        result += line_result[-1]

    print(result)


start = time.perf_counter()
part1()
print(time.perf_counter() - start)


def extend_line_to_left(line):
    if all(i == line[0] for i in line):
        return line + [line[0]]

    difference_list = []

    for i in range((len(line)-1)):
        difference_list.append(line[i+1] - line[i])

    next_line = extend_line_to_left(difference_list)

    return [line[0] - next_line[0]] + line


def part2():
    data = open("adventofcode2023\day9\input.txt",
                "r").read().strip().split("\n")
    result = 0

    for line in range(len(data)):
        line_result = data[line].split()
        line_result = list(map(int, line_result))

        line_result = extend_line_to_left(line_result)

        result += line_result[0]

    print(result)


# start = time.perf_counter()
# part2()
# print(time.perf_counter() - start)
