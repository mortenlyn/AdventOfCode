def part1():
    data = open("adventofcode2020\day3\input.txt").read().splitlines()

    for i in range(len(data)):
        data[i] = list(data[i])

    trees = 0

    for i in range(len(data)):
        if data[i][i*3 % len(data[i])] == "#":
            trees += 1

    print(trees)


# part1()


def part2():
    data = open("adventofcode2020\day3\input.txt").read().splitlines()

    for i in range(len(data)):
        data[i] = list(data[i])

    trees1 = 0
    trees2 = 0
    trees3 = 0
    trees4 = 0
    trees5 = 0

    for i in range(len(data)):
        if data[i][i % len(data[i])] == "#":
            trees1 += 1

    for i in range(len(data)):
        if data[i][i*3 % len(data[i])] == "#":
            trees2 += 1

    for i in range(len(data)):
        if data[i][i*5 % len(data[i])] == "#":
            trees3 += 1

    for i in range(len(data)):
        if data[i][i*7 % len(data[i])] == "#":
            trees4 += 1

    for i in range(0, len(data), 2):
        if data[i][i//2 % len(data[i])] == "#":
            trees5 += 1

    print(trees1 * trees2 * trees3 * trees4 * trees5)


part2()
