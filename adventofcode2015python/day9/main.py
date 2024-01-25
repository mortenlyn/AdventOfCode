def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_paths(graph, node, end, path)
            for new_path in new_paths:
                if len(new_path) == len(graph.keys()):
                    paths.append(new_path)
    return paths


def part1():
    data = open("adventofcode2015python\day9\input.txt").read(
    ).strip().split("\n")

    d = {}

    for line in data:
        line = line.split(" = ")
        cities = line[0].split(" to ")
        if cities[0] in d:
            d[cities[0]][cities[1]] = int(line[1])
        else:
            d[cities[0]] = {cities[1]: int(line[1])}

        if cities[1] in d:
            d[cities[1]][cities[0]] = int(line[1])
        else:
            d[cities[1]] = {cities[0]: int(line[1])}

    paths = []
    for key in d.keys():
        for key2 in d.keys():
            if key != key2:
                paths += find_paths(d, key, key2)

    distances = []
    for path in paths:
        distance = 0
        for i in range(len(path) - 1):
            distance += d[path[i]][path[i + 1]]
        distances.append(distance)

    print(min(distances))


part1()


def part2():
    data = open("adventofcode2015python\day9\input.txt").read(
    ).strip().split("\n")

    d = {}

    for line in data:
        line = line.split(" = ")
        cities = line[0].split(" to ")
        if cities[0] in d:
            d[cities[0]][cities[1]] = int(line[1])
        else:
            d[cities[0]] = {cities[1]: int(line[1])}

        if cities[1] in d:
            d[cities[1]][cities[0]] = int(line[1])
        else:
            d[cities[1]] = {cities[0]: int(line[1])}

    paths = []
    for key in d.keys():
        for key2 in d.keys():
            if key != key2:
                paths += find_paths(d, key, key2)

    distances = []
    for path in paths:
        distance = 0
        for i in range(len(path) - 1):
            distance += d[path[i]][path[i + 1]]
        distances.append(distance)

    print(max(distances))


part2()
