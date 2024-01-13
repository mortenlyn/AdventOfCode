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


def toggle2(x1, x2, y1, y2, lights):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i, j) not in lights:
                lights[(i, j)] = 2
            else:
                lights[(i, j)] += 2


def turn_on2(x1, x2, y1, y2, lights):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i, j) not in lights:
                lights[(i, j)] = 1
            else:
                lights[(i, j)] += 1


def turn_off2(x1, x2, y1, y2, lights):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i, j) in lights and lights[(i, j)] > 0:
                lights[(i, j)] -= 1


def calculate_total_intensity(lights):
    return sum(lights.values())


def part2():
    data = open("adventofcode2015python\day6\input.txt",
                "r").read().strip().split("\n")
    data = [i.split(" ") for i in data]

    lights = {}

    for i in data:
        if i[0] == "toggle":
            x1, y1 = map(int, i[1].split(","))
            x2, y2 = map(int, i[3].split(","))
            toggle2(x1, x2, y1, y2, lights)
        elif i[1] == "on":
            x1, y1 = map(int, i[2].split(","))
            x2, y2 = map(int, i[4].split(","))
            turn_on2(x1, x2, y1, y2, lights)
        else:
            x1, y1 = map(int, i[2].split(","))
            x2, y2 = map(int, i[4].split(","))
            turn_off2(x1, x2, y1, y2, lights)

    total_intensity = calculate_total_intensity(lights)
    print(total_intensity)


part2()
