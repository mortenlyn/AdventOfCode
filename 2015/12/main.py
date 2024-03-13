import json
import re


def part1():
    data = open("input.txt").read().strip()

    allnums = (list(map(int, re.findall(r'[-+]?[.]?[\d]+', data))))

    result = sum(allnums)

    print(result)


# part1()


def find_red(something):
    if type(something) == int:
        return something

    if type(something) == list:
        return sum(find_red(elem) for elem in something)

    if type(something) == dict:
        if "red" in something.values():
            return 0
        return find_red(list(something.values()))

    return 0


def part2():
    data = open("input.txt").read().strip()

    parsed_data = json.loads(data)

    result = find_red(parsed_data)

    print(result)


part2()
