def part1():
    data = open("adventofcode2023\day4\input.txt",
                "r").read().strip().split("\n")
    result = 0
    for line in range(len(data)):
        data[line] = data[line].split("|")
        for elem in range(len(data[line])):
            data[line][elem] = data[line][elem].split()

    for line in data:
        winning = line[0][2:]
        my_num = line[1]

        multiplier = -1
        for elem in my_num:
            if elem in winning:
                multiplier += 1
        if not multiplier == -1:
            result += 2**multiplier

    print(result)


# part1()

def part2():
    data = open("adventofcode2023\day4\input.txt",
                "r").read().strip().split("\n")
    result = 0

    for line in range(len(data)):
        data[line] = data[line].split("|")
        for elem in range(len(data[line])):
            data[line][elem] = data[line][elem].split()

    dp_lst = [0] * len(data)

    for line_index in range(len(data)):
        winning = data[line_index][0][2:]
        my_num = data[line_index][1]

        total_wins = 0
        for elem in my_num:
            if elem in winning:
                total_wins += 1
        for i in range(line_index + 1, line_index + total_wins + 1):
            dp_lst[i] += 1

        result += 1

        for elem in range(dp_lst[line_index]):
            for i in range(line_index + 1, line_index + total_wins + 1):
                dp_lst[i] += 1
            result += 1

    print(result)


part2()
