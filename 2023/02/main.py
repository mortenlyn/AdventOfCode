import re


def check(list1, val):
    return (all(x <= val for x in list1))


def part1():
    data = open("input.txt",
                "r").read().strip().split("\n")
    result = 0

    for i in data:
        green = []
        red = []
        blue = []

        green = list(map(int, re.findall(r'(\d+) green', i)))
        red = list(map(int, re.findall(r'(\d+) red', i)))
        blue = list(map(int, re.findall(r'(\d+) blue', i)))

        if check(green, 13) and check(red, 12) and check(blue, 14):
            result += int((re.findall(r'Game (\d+)', i))[0])

    print(result)


part1()


def check2(list1):
    return (max(list1))


def part2():
    data = open("input.txt",
                "r").read().strip().split("\n")
    result = 0

    for i in data:
        result += (check2(list(map(int, re.findall(r'(\d+) green', i))))) * (
            check2(list(map(int, re.findall(r'(\d+) red', i))))) * (
                check2(list(map(int, re.findall(r'(\d+) blue', i)))))

    print(result)


part2()
