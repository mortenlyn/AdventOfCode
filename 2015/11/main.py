import re
import string


def first_req(data):
    return any(tripple in data for tripple in (string.ascii_lowercase[i:i+3] for i in range(len(string.ascii_lowercase) - 2)))

    # for i in range(len(data) - 2):
    #     current_letter = ord(data[i])
    #     next_letter = ord(data[i+1])
    #     second_next_letter = ord(data[i+2])
    #     if (next_letter == (current_letter + 1)) and (second_next_letter == (next_letter + 1)):
    #         return True

    # return False


def second_req(data):
    return not any(let in data for let in "iol")


def third_req(data):
    return len(re.findall(r".*(.)\1.*(.)\2.*", data)) != 0


def part1():
    data = [*"hxbxwxba"]

    reversed_data = list(reversed(data))

    while not (first_req("".join(data)) and second_req("".join(data)) and third_req("".join(data))):
        reversed_data[0] = chr(ord(reversed_data[0]) + 1)

        for i in range(len(reversed_data)):
            if ord(reversed_data[i]) == 123:
                reversed_data[i] = "a"
                reversed_data[i+1] = chr(ord(reversed_data[i+1]) + 1)

        data = list(reversed(reversed_data))

    return "".join(data)

first_string = part1()
print("Part 1:", first_string)


def part2():
    data = [*first_string]

    reversed_data = list(reversed(data))
    first = True
    while True:
        if (first_req("".join(data)) and second_req("".join(data)) and third_req("".join(data))):
            if not first:
                return "".join(data)
            first = not first
        reversed_data[0] = chr(ord(reversed_data[0]) + 1)

        for i in range(len(reversed_data)):
            if ord(reversed_data[i]) == 123:
                reversed_data[i] = "a"
                reversed_data[i+1] = chr(ord(reversed_data[i+1]) + 1)

        data = list(reversed(reversed_data))


print("Part 2:", part2())
