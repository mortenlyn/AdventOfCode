def update_universe(current_universe):
    updated_rows = []
    for row in current_universe:
        if all(x == "." for x in row):
            updated_rows.append(row)
            updated_rows.append(row)
        else:
            updated_rows.append(row)

    transposed_data = list(map(list, zip(*updated_rows)))

    columns_to_duplicate = [all(x == "." for x in column)
                            for column in transposed_data]

    updated_columns = []
    for column_idx, column in enumerate(transposed_data):
        if columns_to_duplicate[column_idx]:
            for _ in range(2):
                updated_columns.append(column)
        else:
            updated_columns.append(column)

    return list(map(''.join, zip(*updated_columns)))


def give_number_to_galaxy(input_list):
    coordinates = []
    for i in range(len(input_list)):
        line = input_list[i]
        for char in range(len(line)):
            if line[char] == "#":
                coordinates.append((i, 1 + char))
    return coordinates


def find_manhattan_distance(coordinates):
    result = 0
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            result += abs(x1 - x2) + abs(y1 - y2)

    return result


def part1():
    data = open("adventofcode2023\day11\input.txt",
                "r").read().strip().split("\n")

    galaxy_coordinates = give_number_to_galaxy(update_universe(data))
    print(find_manhattan_distance(galaxy_coordinates))


# part1()

def update_universe2(current_universe):
    updated_rows = []
    for row in current_universe:
        if all(x == "." for x in row):
            updated_rows.append(["1000000"] * len(row))
        else:
            updated_rows.append(row)

    return process_columns(updated_rows)


def process_columns(updated_rows):
    transposed_data = list(map(list, zip(*updated_rows)))

    updated_columns = []

    for row in transposed_data:
        if all((x == "." or x == "1000000") for x in row):
            updated_columns.append(["1000000"] * len(row))
        else:
            updated_columns.append(row)

    return updated_columns


def find_coordinates(universe):
    coordinates = []
    y = 0
    for i in range(len(universe)):
        x = 0
        line = universe[i]
        if all(x == "1000000" for x in line):
            y += 1000000
            continue
        else:
            y += 1

        for char in range(len(line)):
            if line[char] == "1000000":
                x += 1000000
            else:
                x += 1

            if line[char] == "#":
                coordinates.append((x, y))

    return coordinates


def part2():
    data = open("adventofcode2023\day11\input.txt",
                "r").read().strip().split("\n")

    data = [list(line) for line in data]
    updated_universe = update_universe2(data)
    coordinates = find_coordinates(updated_universe)
    print(find_manhattan_distance(coordinates))


part2()
