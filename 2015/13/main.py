from itertools import permutations


def get_combinations(people):
    return [list(permutation) for permutation in permutations(people)]


def get_happiness(seating, seating_dict):
    happiness = 0

    for i in range(len(seating)):
        if i == 0:
            for person in seating_dict[seating[i]]:
                if seating[i + 1] in person:
                    happiness += person[seating[i + 1]]
                if seating[-1] in person:
                    happiness += person[seating[-1]]
        elif i == len(seating) - 1:
            for person in seating_dict[seating[i]]:
                if seating[0] in person:
                    happiness += person[seating[0]]
                if seating[i - 1] in person:
                    happiness += person[seating[i - 1]]
        else:
            for person in seating_dict[seating[i]]:
                if seating[i + 1] in person:
                    happiness += person[seating[i + 1]]
                if seating[i - 1] in person:
                    happiness += person[seating[i - 1]]

    return happiness


def part1():
    data = open("input.txt").read().strip().split("\n")

    data = [data[i].split(" ") for i in range(len(data))]

    seating_dict = {}

    for line in data:
        if line[0] in seating_dict:
            if line[2] == "gain":
                seating_dict[line[0]].append({line[-1].strip("."): int(line[3])})
            else:
                seating_dict[line[0]].append({line[-1].strip("."): -int(line[3])})

        else:
            if line[2] == "gain":
                seating_dict[line[0]] = [{line[-1].strip("."): int(line[3])}]
            else:
                seating_dict[line[0]] = [{line[-1].strip("."): -int(line[3])}]

    all_people = list(seating_dict.keys())

    all_combinations = get_combinations(all_people)

    max_happiness = 0

    for combination in all_combinations:
        happiness = get_happiness(combination, seating_dict)
        if happiness > max_happiness:
            max_happiness = happiness

    print("Part 1:", max_happiness)


part1()


def part2():
    data = open("input.txt").read().strip().split("\n")

    data = [data[i].split(" ") for i in range(len(data))]

    seating_dict = {}

    for line in data:
        if line[0] in seating_dict:
            if line[2] == "gain":
                seating_dict[line[0]].append({line[-1].strip("."): int(line[3])})
            else:
                seating_dict[line[0]].append({line[-1].strip("."): -int(line[3])})

        else:
            if line[2] == "gain":
                seating_dict[line[0]] = [{line[-1].strip("."): int(line[3])}]
            else:
                seating_dict[line[0]] = [{line[-1].strip("."): -int(line[3])}]

    seating_dict["me"] = []

    all_people = list(seating_dict.keys())

    all_combinations = get_combinations(all_people)

    max_happiness = 0

    for combination in all_combinations:
        happiness = get_happiness(combination, seating_dict)
        if happiness > max_happiness:
            max_happiness = happiness

    print("Part 2:", max_happiness)


part2()
