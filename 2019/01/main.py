import math


def part1():
    data = open("input.txt").read().strip().split("\n")

    amount_fuel = 0

    for elem in data:
        amount_fuel += math.floor((int(elem)/3)) - 2

    print("Part 1:", amount_fuel)


part1()


def part2():
    data = open("input.txt").read().strip().split("\n")

    amount_fuel = 0

    for elem in data:
        new_fuel = math.floor((int(elem)/3)) - 2
        while new_fuel > 0:
            amount_fuel += new_fuel
            new_fuel = math.floor((int(new_fuel)/3)) - 2

    print("Part 2:", amount_fuel)


part2()
