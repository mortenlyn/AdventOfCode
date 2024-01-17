import re
import collections


def part1():
    data = open(
        "adventofcode2016/day4/input.txt").read().strip().split("\n")

    result = 0

    for line in range(len(data)):
        data[line] = data[line].strip("]")
        data[line] = re.split(r'-|\[', data[line])

    for room in range(len(data)):
        counter = collections.Counter()

        for name in data[room][:-2]:
            counter.update(name)

        check_sum = "".join(x[0] for x in sorted(
            counter.most_common(), key=lambda x: (-x[1], x[0]))[:5])

        result += int(data[room][-2]) if check_sum == data[room][-1] else 0

    print(result)


# part1()

def part2():
    data = open(
        "adventofcode2016/day4/input.txt").read().strip().split("\n")

    for line in range(len(data)):
        data[line] = data[line].strip("]")
        data[line] = re.split(r'-|\[', data[line])

    for line in range(len(data)):
        switch = int(data[line][-2]) % 26

        for word in range(len(data[line]) - 2):
            s = ""
            for letter in range(len(data[line][word])):
                new_letter = ord(data[line][word][letter]) + switch
                if ord("z") < new_letter:
                    new_letter -= 26
                s += chr(new_letter)
            data[line][word] = s

    for line in data:
        if "pole" in " ".join(line):
            print(line[-2])


# part2()
