def part1():
    data = open("input.txt").read().strip().split("\n")

    result = 0

    for line in data:
        rows = [i for i in range(0, 128)]
        columns = [i for i in range(0, 8)]

        for letter in line[:-3]:
            if letter == "F":
                rows = rows[:len(rows)//2]
            elif letter == "B":
                rows = rows[len(rows)//2:]

        for letter in line[-3:]:
            if letter == "R":
                columns = columns[len(columns)//2:]
            elif letter == "L":
                columns = columns[:len(columns)//2]

        result = max(result, (rows[0] * 8) + columns[0])

    print(result)


part1()


def part2():
    data = open("input.txt").read().strip().split("\n")

    result = []

    for line in data:
        rows = [i for i in range(0, 128)]
        columns = [i for i in range(0, 8)]

        for letter in line[:-3]:
            if letter == "F":
                rows = rows[:len(rows)//2]
            elif letter == "B":
                rows = rows[len(rows)//2:]

        for letter in line[-3:]:
            if letter == "R":
                columns = columns[len(columns)//2:]
            elif letter == "L":
                columns = columns[:len(columns)//2]

        result.append((rows[0] * 8) + columns[0])

    result = sorted(result)

    for i in range(len(result)):
        if result[i + 1] != result[i] + 1:
            print(result[i] + 1)
            break


part2()
