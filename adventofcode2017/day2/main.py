def part1():
    data = open("adventofcode2017\day2\input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = list(map(int, data[i].split("\t")))

    for row in data:
        result += (max(row) - min(row))

    print("Part1:", result)


part1()


def part2():
    data = open("adventofcode2017\day2\input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = list(map(int, data[i].split("\t")))

    for row in data:
        for el1 in row:
            for elem in row:
                if (el1 != elem) and (el1 % elem) == 0:
                    result += el1 // elem

    print("Part2:", result)


part2()
