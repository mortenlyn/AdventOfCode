def manhattan_distance(x, y):
    return abs(x) + abs(y)


def part1():
    data = int(open("input.txt").read().strip())

    x = 0
    y = 0

    counter = 1
    num = 1
    check = 0
    while num < data:
        for _ in range(2):
            for _ in range(counter):
                if num >= data:
                    break
                if check % 4 == 0:
                    x += 1
                elif check % 4 == 1:
                    y += 1
                elif check % 4 == 2:
                    x -= 1
                elif check % 4 == 3:
                    y -= 1
                num += 1

            check += 1
        counter += 1

    print(manhattan_distance(x, y))


part1()


def part2():
    data = int(open("input.txt").read().strip())

    d = {}
    x = 0
    y = 0

    counter = 1
    check = 0
    num = 1
    while num < data:
        for _ in range(2):
            for _ in range(counter):
                d[(x, y)] = num
                if num > data:
                    break
                if check % 4 == 0:
                    x += 1
                elif check % 4 == 1:
                    y += 1
                elif check % 4 == 2:
                    x -= 1
                elif check % 4 == 3:
                    y -= 1

                num = 0
                for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    num += d.get((x + dx, y + dy), 0)

            check += 1
        counter += 1

    print(d[(x, y)])


part2()
