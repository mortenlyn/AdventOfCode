def part1():
    data = open("input.txt").read().strip().split("\n\n")

    result = 0

    for line in range(len(data)):
        data[line] = data[line].split("\n")

    for line in data:
        unique = set()
        for elem in line:
            unique.update(elem)

        result += len(unique)

    print(result)


# part1()


def part2():
    data = open("input.txt").read().strip().split("\n\n")

    result = 0

    for line in range(len(data)):
        data[line] = data[line].split("\n")

    for line in data:
        if len(line) == 1:
            result += len(set(line[0]))
        else:
            unique = set()
            for elem in line:
                unique.update(elem)

            for elem in line[0:]:
                unique = unique.intersection(set(elem))

            result += len(unique)

    print(result)


part2()
