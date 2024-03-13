def opcode1(pos1, pos2, resultpos, data):
    new_value = data[pos1] + data[pos2]

    data[resultpos] = new_value

    return data


def opcode2(pos1, pos2, resultpos, data):
    new_value = data[pos1] * data[pos2]

    data[resultpos] = new_value

    return data


def opcode99(data):
    print(data)
    print(data[0])


def part1():
    data = open("input.txt").read().strip().split(",")

    data = list(map(int, data))

    data[1] = 12
    data[2] = 2

    i = 0

    while True:
        opcode = data[i]
        if opcode == 99:
            data = opcode99(data)
            break
        pos1 = data[i+1]
        pos2 = data[i+2]
        resultpos = data[i+3]

        i += 4

        if opcode == 1:
            data = opcode1(pos1, pos2, resultpos, data)
        if opcode == 2:
            data = opcode2(pos1, pos2, resultpos, data)
        else:
            continue


# part1()

def opcode99CheckOutput(data):
    if data[0] == 19690720:
        return True
    return False


def part2():
    data = open("input.txt").read().strip().split(",")

    data = list(map(int, data))

    noun = 0
    verb = 0

    i = 0

    temp_data = data[:]

    for j in range(100):
        noun = j
        for k in range(100):
            verb = k
            temp_data[1] = noun
            temp_data[2] = verb
            while True:
                opcode = temp_data[i]
                if opcode == 99:
                    if opcode99CheckOutput(temp_data):
                        print(100 * noun + verb)
                        exit()

                    temp_data = data[:]

                    i = 0

                    break

                pos1 = temp_data[i+1]
                pos2 = temp_data[i+2]
                resultpos = temp_data[i+3]

                i += 4

                if opcode == 1:
                    temp_data = opcode1(pos1, pos2, resultpos, temp_data)
                if opcode == 2:
                    temp_data = opcode2(pos1, pos2, resultpos, temp_data)
                else:
                    continue


part2()
