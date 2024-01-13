def turn_on(x1, y1, x2, y2, on_set):
    on_set.update((x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))
    return on_set


def turn_off(x1, y1, x2, y2, on_set):
    on_set.difference_update((x, y) for x in range(x1, x2 + 1)
                             for y in range(y1, y2 + 1))
    return on_set


def toggle(x1, y1, x2, y2, on_set):
    on_set.symmetric_difference_update((x, y) for x in range(x1, x2 + 1)
                                       for y in range(y1, y2 + 1))
    return on_set


def part1():
    data = open("adventofcode2015python\day6\input.txt",
                "r").read().strip().split("\n")
    data = [i.split(" ") for i in data]
    print(data)
    on_set = set()

    for line in data:
        if line[0] == "toggle":
            x1, y1 = map(int, line[1].split(","))
            x2, y2 = map(int, line[3].split(","))
            toggle(x1, y1, x2, y2, on_set)
            continue

        x1, y1 = map(int, line[2].split(","))
        x2, y2 = map(int, line[4].split(","))

        if line[1] == "on":
            turn_on(x1, y1, x2, y2, on_set)
        elif line[1] == "off":
            turn_off(x1, y1, x2, y2, on_set)

    print(len(on_set))


# part1()

def toggle(x1, x2, y1, y2, counter):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            counter += 2

    return counter


def turn_on(x1, x2, y1, y2, counter):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            counter += 1

    return counter


def turn_off(x1, x2, y1, y2, counter):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if counter > 0:
                counter -= 1

    return counter


def part2():
    data = open("adventofcode2015python\day6\input.txt",
                "r").read().strip().split("\n")
    data = [i.split(" ") for i in data]

    counter = 0

    for i in data:
        if i[0] == "toggle":
            x1, y1 = map(int, i[1].split(","))
            x2, y2 = map(int, i[3].split(","))
            counter = toggle(x1, x2, y1, y2, counter)
            continue
        if i[1] == "on":
            x1, y1 = map(int, i[2].split(","))
            x2, y2 = map(int, i[4].split(","))
            counter = turn_on(x1, x2, y1, y2,  counter)
            continue
        else:
            x1, y1 = map(int, i[2].split(","))
            x2, y2 = map(int, i[4].split(","))
            counter = turn_off(x1, x2, y1, y2,  counter)
            continue

    print(counter)


part2()
