def parse_string(string):
    count = 0

    string_list = ([*string])[1:-1]

    if len(string_list) == 0:
        return 0

    index = 0
    while index < len(string_list):
        if string_list[index] == "\\":
            match string_list[index + 1]:
                case "\"":
                    count += 1
                    index += 2
                case "\\":
                    count += 1
                    index += 2
                case "x":
                    count += 1
                    index += 4
        else:
            index += 1
            count += 1

    return count


def part1():
    data = open("input.txt").read(
    ).strip().split("\n")

    num_char_string = 0

    for line in data:
        num_char_string += len(line)

    num_char_mem = 0

    for line in data:
        num_char_mem += parse_string(line)

    print("Part 1:", num_char_string - num_char_mem)


part1()


def new_parse_string(string):
    count = 4

    string_list = ([*string])

    if len(string_list) == 0:
        print(string_list)
        print(count)
        return count

    index = 0
    while index < len(string_list):
        if string_list[index] == "\\":
            match string_list[index + 1]:
                case "\"":
                    count += 4
                    index += 2
                case "\\":
                    count += 4
                    index += 2
                case "x":
                    count += 5
                    index += 4
        else:
            index += 1
            count += 1

    return count


def part2():
    data = open("input.txt").read(
    ).strip().split("\n")

    num_char_string = 0

    for line in data:
        num_char_string += len(line)

    num_char_mem = 0

    for line in data:
        num_char_mem += new_parse_string(line)

    print("Part 2:", num_char_mem - num_char_string)


part2()
