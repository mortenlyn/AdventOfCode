import re


def part1():
    data = open("input.txt").read().strip().split("\n")

    result = 0

    for i in data:
        a, b, c = map(int, i.split())

        if a + b > c and a + c > b and b + c > a:
            result += 1

    print(result)


# part1()


def part2():
    data = open("input.txt").read().strip().split("\n")

    result = 0

    for i in range(0, len(data) - 2, 3):
        for j in range(3):
            line_split1 = list(map(int, re.findall(r"\d+", data[i])))
            line_split2 = list(map(int, re.findall(r"\d+", data[i + 1])))
            line_split3 = list(map(int, re.findall(r"\d+", data[i + 2])))

            a = line_split1[j]
            b = line_split2[j]
            c = line_split3[j]

            if a + b > c and a + c > b and b + c > a:
                result += 1

    print(result)


part2()
