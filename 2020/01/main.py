def part1():
    data = open("input.txt").read().strip().split("\n")

    data = list(map(int, data))

    for i in range(len(data)):
        for j in range(len(data[i:])):
            if data[i] + data[j] == 2020:
                return data[i]*data[j]


# print(part1())


def part2():
    data = open("input.txt").read().strip().split("\n")

    data = list(map(int, data))

    for i in range(len(data)):
        for j in range(len(data)):
            for h in range(len(data)):
                if data[i] + data[j] + data[h] == 2020:
                    return data[i]*data[j]*data[h]


print(part2())
