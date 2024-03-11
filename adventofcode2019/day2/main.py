def opcode1(pos1, pos2, resultpos, data):
    new_value = data[pos1] + data[pos2]

    print(data)

    data[resultpos] = new_value

    print(data)

    return data


def opcode2(pos1, pos2, resultpos, data):
    new_value = pos1 * pos2

    data[resultpos] = new_value

    return data


def opcode99(data):
    print(data[0])


def part1():
    data = open("adventofcode2019\day2\input.txt").read().strip().split(",")

    data = list(map(int, data))

    print(len(data))
    for i in range(0, len(data) - 3, 4):
        opcode = data[i]
        pos1 = data[i+1]
        pos2 = data[i+2]
        resultpos = data[i+3]

        print(data[i], data[i+1], data[i+2], data[i+3])

        if opcode == 1:
            data = opcode1(pos1, pos2, resultpos, data)
        if opcode == 2:
            data = opcode2(pos1, pos2, resultpos, data)
        if opcode == 99:
            data = opcode99(data)
            break
        else:
            continue


part1()
