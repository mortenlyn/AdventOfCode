import re


def checkContains(value, d):
    count = 0
    if value[0][1] == "no other":
        return False

    for tup in value:
        if tup[1] == "shiny gold":
            return True

    for tup in value:
        if checkContains(d[tup[1]], d):
            return True

    return False


def part1():
    data = open("adventofcode2020\day7\input.txt").read().strip().split("\n")

    d = {}

    result = 0

    for line in range(len(data)):
        data[line] = re.findall(r"(\d+)? ?(\w+ \w+) bags?", data[line])

    for line in data:
        d[line[0][1]] = []
        for tup in line[1:]:
            d[line[0][1]].append(tup)

    for key, value in d.items():
        if key == "shiny gold":
            continue
        if checkContains(value, d):
            result += 1

    print(result)


part1()


def totalBags(tup, d):
    count = 1
    for i in d[tup[1]]:
        if i[1] == "no other":
            continue

        count += (int(i[0]) * totalBags(i, d))

    return count


def part2():
    data = open("adventofcode2020\day7\input.txt").read().strip().split("\n")

    d = {}

    result = 0

    for line in range(len(data)):
        data[line] = re.findall(r"(\d+)? ?(\w+ \w+) bags?", data[line])

    for line in data:
        d[line[0][1]] = []
        for tup in line[1:]:
            d[line[0][1]].append(tup)

    for tup in d["shiny gold"]:
        result += (int(tup[0]) * totalBags(tup, d))

    print(result)


part2()
