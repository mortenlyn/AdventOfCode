def next_num(num):
    new_num = ""

    counter = 1
    if len(num) == 1:
        new_num += str(counter) + num
        return new_num

    for i in range(len(num)):
        if (i+1 == len(num)):
            new_num += (str(counter) + num[i])
            return new_num

        if num[i+1] == num[i]:
            counter += 1
        else:
            new_num += (str(counter) + num[i])
            counter = 1


def part1and2():
    data = "1113122113"

    for _ in range(40):
        data = next_num(data)

    print("Part 1:", len(data))

    data = "1113122113"

    for _ in range(50):
        data = next_num(data)

    print("Part 2:", len(data))


part1and2()
