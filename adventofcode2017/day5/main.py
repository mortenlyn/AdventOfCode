def part1():
    data = open("adventofcode2017\day5\input.txt").read().strip().split("\n")

    increment_count = {}

    result = 0

    data = list(map(int, data))

    i = 0
    while i < len(data):
        result += 1
        current_index = i
        i += data[current_index]

        if current_index not in increment_count:
            increment_count[current_index] = 1

        else:
            i += increment_count[current_index]
            increment_count[current_index] += 1

    print("Part 1:", result)


part1()


def part2():
    data = open("adventofcode2017\day5\input.txt").read().strip().split("\n")

    increment_count = {}

    result = 0

    data = list(map(int, data))

    i = 0
    while i < len(data):
        result += 1
        current_index = i
        i += data[current_index]

        if current_index not in increment_count:
            if data[current_index] >= 3:
                increment_count[current_index] = -1
            else:
                increment_count[current_index] = 1

        else:
            i += increment_count[current_index]
            if data[current_index] + increment_count[current_index] >= 3:
                increment_count[current_index] -= 1
            else:
                increment_count[current_index] += 1

    print("Part 2:", result)


part2()
