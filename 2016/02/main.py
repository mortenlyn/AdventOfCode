def part1():
    data = open("input.txt",
                "r").read().strip().split("\n")

    current = 5
    result = []

    for i in data:
        for letter in i:
            if letter == "U":
                if current > 3:
                    current -= 3
            elif letter == "D":
                if current < 7:
                    current += 3
            elif letter == "L":
                if current not in [1, 4, 7]:
                    current -= 1
            else:
                if current not in [3, 6, 9]:
                    current += 1

        result.append(current)

    print("".join(map(str, result)))


# part1()

def part2():
    data = open("input.txt",
                "r").read().strip().split("\n")

    matrix = [["0", "0", "1", "0", "0"], ["0", "2", "3", "4", "0"], [
        "5", "6", "7", "8", "9"], ["0", "A", "B", "C", "0"], ["0", "0", "D", "0", "0"]]
    y, x = 2, 0
    result = []

    for i in data:
        for letter in i:
            if letter == "U":
                if (y - 1) >= 0 and matrix[y - 1][x] != "0":
                    y -= 1
            if letter == "D":
                if (y + 1) < len(matrix) and matrix[y + 1][x] != "0":
                    y += 1
            if letter == "R":
                if (x + 1) < len(matrix[y]) and matrix[y][x+1] != "0":
                    x += 1
            if letter == "L":
                if (x - 1) >= 0 and matrix[y][x - 1] != "0":
                    x -= 1

        result.append(matrix[y][x])

    print("".join(map(str, result)))


part2()
