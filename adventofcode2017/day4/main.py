def part1():
    data = open("adventofcode2017\day4\input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = data[i].split(" ")

    for line in data:
        if len(line) == len(set(line)):
            result += 1

    print("Part 1:", result)


part1()


def part2():
    data = open("adventofcode2017\day4\input.txt").read().strip().split("\n")

    result = 0

    for i in range(len(data)):
        data[i] = data[i].split(" ")

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = [*data[i][j]]

    for line in data:
        flag = False
        for i in range(len(line)):
            check = sorted(line[i])
            for word in line[i+1:]:
                if check == sorted(word):
                    flag = True
            if flag == True:
                break
        if flag == False:
            result += 1

    print("Part 2:", result)


part2()
