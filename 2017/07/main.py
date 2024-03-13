from collections import Counter


def part1():
    data = open("input.txt").read().strip().split("\n")

    l = []

    for line in data:
        if "-> " in line:
            leaves = line.split("-> ")[1].split(", ")
            for leaf in leaves:
                if leaf not in l:
                    l.append(leaf)

    data = [line.split(" ") for line in data]

    for line in data:
        if line[0] not in l:
            return line[0]


print("Part 1:", part1())


def weight(leaf, leaf_mapping, leaf_weight):
    if leaf not in leaf_mapping:
        return leaf_weight[leaf]

    return leaf_weight[leaf] + sum(weight(new_leaf, leaf_mapping, leaf_weight) for new_leaf in leaf_mapping[leaf])


def part2():
    data = open("input.txt").read().strip().split("\n")

    leaf_mapping = {}
    leaf_weight = {}

    for line in data:
        if "-> " in line:
            leaves = line.split("-> ")[1].split(", ")
            leaf_mapping[line.split(" ")[0]] = leaves

    data = [line.split(" ") for line in data]

    for line in data:
        leaf_weight[line[0]] = int(line[1][1:-1])

    prev = None
    imposter = part1()
    while True:
        weights = {}
        for value in leaf_mapping[imposter]:
            weights[value] = weight(
                value, leaf_mapping, leaf_weight)

        temp = Counter(weights)

        if len(set(x[1] for x in temp.most_common())) == 1:
            print("Part 2:", leaf_weight[prev.most_common()[0][0]] +
                  prev.most_common()[-1][1] - prev.most_common()[0][1])
            break

        prev = temp
        imposter = temp.most_common()[0][0]


part2()
