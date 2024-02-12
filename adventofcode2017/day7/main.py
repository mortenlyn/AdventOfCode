from collections import Counter


def part1():
    data = open("adventofcode2017\day7\input.txt").read().strip().split("\n")

    l = []

    for line in data:
        if "-> " in line:
            leaves = line.split("-> ")[1].split(", ")
            for leaf in leaves:
                if leaf not in l:
                    l.append(leaf)

    data = [line.split(" ") for line in data]

    for line in data:
        if line[0] not in l:
            return line[0]


print(part1())
