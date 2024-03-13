def part1():
    data = open("input.txt").read(
    ).strip().split("\n")

    data = [data[i].split(" ") for i in range(len(data))]

    seating_dict = {}

    for line in data:
        if line[0] in seating_dict:
            if line[2] == "gain":
                seating_dict[line[0]].append(
                    {line[-1].strip("."): int(line[3])})
            else:
                seating_dict[line[0]].append(
                    {line[-1].strip("."): -int(line[3])})

        else:
            if line[2] == "gain":
                seating_dict[line[0]] = [{line[-1].strip("."): int(line[3])}]
            else:
                seating_dict[line[0]] = [{line[-1].strip("."): -int(line[3])}]


part1()
