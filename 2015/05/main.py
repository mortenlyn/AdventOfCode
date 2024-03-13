def is_nice_string(string):
    vowles = ["a", "e", "i", "o", "u"]
    naughty_strings = ["ab", "cd", "pq", "xy"]

    if sum(string.count(vowl) for vowl in vowles) >= 3:
        for i in naughty_strings:
            if i in string:
                return False
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return True
    return False


def part1():
    data = open("input.txt",
                "r").read().strip().split("\n")

    print(sum(map(is_nice_string, data)))


part1()


def is_nice_string2(string):
    return (any(string[i] == string[i + 2]
                for i in range(len(string) - 2)) and
            any(string.count(string[i:i+2]) >= 2
                for i in range(len(string) - 1))
            )


def part2():
    data = open("input.txt",
                "r").read().strip().split("\n")

    print(sum(map(is_nice_string2, data)))


def part2():
    return sum(any(string[i] == string[i + 2] for i in range(len(string) - 2)) and
               any(string.count(string[i:i+2]) >= 2 for i in range(len(string) - 1)) for string in open("input.txt").read().strip().split("\n"))


part2()
