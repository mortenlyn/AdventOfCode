def instruction(ins, booklet):
    ins_mapping = {" AND ": lambda x, y: x & y,
                   " OR ": lambda x, y: x | y,
                   " LSHIFT ": lambda x, y: x << y,
                   " RSHIFT ": lambda x, y: x >> y,
                   "NOT ": lambda x: format(x, "016b")}

    if len(ins[0]) < 3 and not ins[0].isdigit():
        if ins[0] not in booklet:
            return booklet
        booklet[ins[1]] = booklet[ins[0]]

    for key in ins_mapping.keys():
        if key in ins[0]:
            if key == "NOT ":
                x = ins[0].replace("NOT ", "")

                if x not in booklet:
                    return booklet
                binary = ins_mapping[key](
                    int(booklet[x]))
                booklet[ins[1]] = (1 << 16) - 1 - int(binary, 2)

                return booklet

            split_ins = ins[0].split(key)
            x, y = split_ins[0], split_ins[1]

            if y.isdigit():
                if x not in booklet:
                    return booklet
                booklet[ins[1]] = ins_mapping[key](booklet[x], int(y))
            elif x.isdigit():
                if y not in booklet:
                    return booklet
                booklet[ins[1]] = ins_mapping[key](int(x), booklet[y])
            else:
                if x not in booklet or y not in booklet:
                    return booklet
                booklet[ins[1]] = ins_mapping[key](booklet[x], booklet[y])

    return booklet


def part1():
    data = open("input.txt").read(
    ).strip().split("\n")

    booklet = {}

    for i in range(len(data)):
        data[i] = data[i].split(" -> ")

    for line in data:
        if line[0].isdigit():
            booklet[line[1]] = int(line[0])

        for line2 in data:
            booklet = instruction(line2, booklet)

    return booklet["a"]


print(part1())


def part2():
    data = open("input.txt").read(
    ).strip().split("\n")

    booklet = {}

    for i in range(len(data)):
        data[i] = data[i].split(" -> ")
    for line in data:
        if line[1] == "b":
            booklet[line[1]] = part1()
            continue
        if line[0].isdigit():
            booklet[line[1]] = int(line[0])

        for line2 in data:
            if line[1] == "b":
                continue
            booklet = instruction(line2, booklet)

    print(booklet["a"])


part2()
