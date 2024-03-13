def part1and2():
    data = open("input.txt").read().strip().split("\t")

    data = list(map(int, data))
    result = 0

    combinations = ["".join(list(map(str, data)))]

    while len(combinations) == len(set(combinations)):
        result += 1
        max_elem = max(data)
        index = data.index(max_elem)

        data[index] = 0
        index += 1

        while max_elem > 0:
            if index > (len(data) - 1):
                index = 0
            data[index] += 1
            max_elem -= 1
            index += 1

        combinations.append("".join(list(map(str, data))))

    print("Part 1:", result)

    for i in range(len(combinations)):
        current = combinations[i]
        for j in combinations[i:]:
            if current == j and i != combinations.index(j):
                print("Part 2:", combinations.index(
                    j, i) - combinations.index(current))


part1and2()
