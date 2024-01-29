def most_common(lst):
    return max(set(lst), key=lst.count)


def part1():
    data = open("adventofcode2016\day6\input.txt").read().strip().split("\n")

    d = {}
    result = ""

    for line in data:
        for i in range(len(line)):
            if i in d:
                d[i].append(line[i])
            else:
                d[i] = [line[i]]

    for l in d.values():
        result += most_common(l)

    print(result)


# part1()


def least_common(lst):
    return min(set(lst), key=lst.count)


def part2():
    data = open("adventofcode2016\day6\input.txt").read().strip().split("\n")

    d = {}
    result = ""

    for line in data:
        for i in range(len(line)):
            if i in d:
                d[i].append(line[i])
            else:
                d[i] = [line[i]]

    for l in d.values():
        print(min(set(l), key=l.count))
        result += least_common(l)

    print(result)


part2()
