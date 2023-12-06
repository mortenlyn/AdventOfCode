import functools
import operator
from tqdm import trange


def part1():
    data = open("adventofcode2023\day6\input.txt",
                "r").read().strip().split("\n")

    result_lst = []

    for line in range(len(data)):
        data[line] = data[line].split()

    for i in range(1, len(data[0])):
        time = int(data[0][i])
        cur_result = 0
        for j in range(time):
            if (time - j) * j > int(data[1][i]):
                cur_result += 1
        result_lst.append(cur_result)

    print(functools.reduce(operator.mul, result_lst, 1))


part1()


def part2():
    data = open("adventofcode2023\day6\input.txt",
                "r").read().strip().split("\n")

    result_lst = []

    for line in range(len(data)):
        data[line] = data[line].split(":")
        data[line][1] = data[line][1].replace(" ", "")

    for i in range(1, len(data[0])):
        time = int(data[0][i])
        cur_result = 0
        for j in trange(time):
            if (time - j) * j > int(data[1][i]):
                cur_result += 1
        result_lst.append(cur_result)

    print(functools.reduce(operator.mul, result_lst, 1))


part2()
