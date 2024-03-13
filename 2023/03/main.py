import re


def checkAdjacent(data, x, y, length, line_num, num):
    if x == 0:
        index_start = x
    else:
        index_start = x - 1

    if y == length:
        index_end = y
    else:
        index_end = y + 1

    for i in range(index_start, index_end):
        if not line_num == 0:
            if not re.match("\.|\d", data[line_num - 1][i]):
                return num

        if not line_num == len(data) - 1:
            if not re.match("\.|\d", data[line_num + 1][i]):
                return num
    return 0


def part1():
    data = open("input.txt",
                "r").read().strip().splitlines()
    lenght_line = len(data[0])
    result = 0

    for i in range(len(data)):
        num = re.finditer("\d+", data[i])
        for j in num:
            num = j.group()

            if not j.start() == 0:
                if not data[i][j.start() - 1] == ".":
                    result += int(num)
                    continue

            if not (j.start() + len(num)) >= lenght_line:
                if not data[i][j.start() + len(num)] == ".":
                    result += int(num)
                    continue

            result += int(checkAdjacent(data, j.start(), (int(j.start()) +
                                                          len(num)), lenght_line, i, num))

    print("Part 1:", result)


part1()


def checkCap(cap):
    if cap <= 2:
        return True
    return False


def checkAdjacent2(data, line_num, index):
    cap = 0
    result = 0
    result_list = []
    while cap <= 2:
        first = 0
        second = 0
        same_line = re.finditer("\d+", data[line_num])

        for i in same_line:
            if (i.start() + len(i.group())) == (index):
                cap += 1
                if not checkCap(cap):
                    return 0
                first = int(i.group())
                result_list.append(first)
            elif i.start() == index + 1:
                cap += 1
                if not checkCap(cap):
                    return 0
                second = int(i.group())
                result_list.append(second)

        if line_num == 0:
            above = []
        else:
            above = re.finditer("\d+", data[line_num - 1])

        if line_num == len(data) - 1:
            below = []
        else:
            below = re.finditer("\d+", data[line_num + 1])

        above_num = 0
        below_num = 0

        if index == 0:
            valid_index = [index, index + 1]
        elif index == len(data[line_num]):
            valid_index = [index - 1, index]
        else:
            valid_index = [index - 1, index, index + 1]

        for i in above:
            for j in range(i.start(), i.start() + len(i.group())):
                if j in valid_index:
                    cap += 1
                    if not checkCap(cap):
                        return 0
                    above_boolean = True
                    above_num = int(i.group())
                    result_list.append(above_num)
                    break

        for i in below:
            for j in range(i.start(), i.start() + len(i.group())):
                if j in valid_index:
                    below_boolean = True
                    cap += 1
                    if not checkCap(cap):
                        return 0
                    below_num = int(i.group())
                    result_list.append(below_num)
                    break

        final_list = []
        for i in result_list:
            if i != 0:
                final_list.append(i)

        if len(final_list) == 2:
            result = final_list[0] * final_list[1]

        return result

    return 0


def part2():
    data = open("input.txt",
                "r").read().strip().splitlines()
    result = 0
    pattern = r'[^\.\d]'

    for i in range(len(data)):
        sign = re.finditer(pattern, data[i])
        for j in sign:
            result += checkAdjacent2(data, i, j.start())

    print("Part 2:", result)


part2()
