def part1():
    data = open("adventofcode2017\day1\input.txt").read().strip()

    sum = 0
    for i in range(len(data)):
        if data[i] == data[i-1]:
            sum += int(data[i])

    print(sum)


part1()


def part2():
    data = open("adventofcode2017\day1\input.txt").read().strip()

    length = len(data)
    sum = 0
    for i in range(len(data)):
        if data[i] == data[(i + length//2) % length]:
            sum += int(data[i])

    print(sum)


part2()
