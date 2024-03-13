import re


def part1():
    data = open("input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = re.split(r"-| ", data[i])

    for i in data:
        l = [num for num in range(int(i[0]), int(i[1]) + 1)]
        counter = 0

        for letter in i[-1]:
            if i[-2][0] == letter:
                counter += 1

        if counter in l:
            result += 1

    print(result)


part1()


def part2():
    data = open("input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = re.split(r"-| ", data[i])

    for i in data:
        a, b = int(i[0]) - 1, int(i[1]) - 1

        if i[-1][a] == i[-2][0]:
            if i[-1][b] == i[-2][0]:
                continue
            result += 1

        if i[-1][b] == i[-2][0]:
            if i[-1][a] == i[-2][0]:
                continue
            result += 1

    print(result)


part2()
