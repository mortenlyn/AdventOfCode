from collections import Counter


def first_req(data):
    for i in range(len(data) - 2):
        current_letter = ord(data[i])
        next_letter = ord(data[i+1])
        second_next_letter = ord(data[i+2])
        if (next_letter == (current_letter + 1)) and (second_next_letter == (next_letter + 1)):
            return True

    return False


def second_req(data):
    for let in ["i", "o", "l"]:
        if let in data:
            return False
    return True


def third_req(data):
    counter = 0
    index = 0

    while index < (len(data)-1):
        if data[index] == data[index + 1]:
            counter += 1
            index += 1
        index += 1

    return counter >= 2


def part1():
    data = ([*"hxbxwxba"])

    reversed_data = list(reversed(data))

    while not (first_req("".join(data)) and second_req("".join(data)) and third_req("".join(data))):
        reversed_data[0] = chr(ord(reversed_data[0]) + 1)

        for i in range(len(reversed_data)):
            if ord(reversed_data[i]) == 123:
                reversed_data[i] = "a"
                reversed_data[i+1] = chr(ord(reversed_data[i+1]) + 1)

        data = list(reversed(reversed_data))

    return "".join(data)


print("Part 1:", part1())


def part2():
    data = ([*"hxbxxzaa"])

    reversed_data = list(reversed(data))

    while not (first_req("".join(data)) and second_req("".join(data)) and third_req("".join(data))):
        reversed_data[0] = chr(ord(reversed_data[0]) + 1)

        for i in range(len(reversed_data)):
            if ord(reversed_data[i]) == 123:
                reversed_data[i] = "a"
                reversed_data[i+1] = chr(ord(reversed_data[i+1]) + 1)

        data = list(reversed(reversed_data))

    return "".join(data)


print("Part 2:", part2())
