
def first():
    inp = open("adventofcode2023\day1\input.txt", "r").read().split("\n")

    result = []

    for i in inp:
        i_len = len(i)
        back_pointer = i_len - 1
        str_result = ""
        str_result1 = ""
        str_result2 = ""

        for j in range((i_len)):
            if (len(str_result1) > 0 and len(str_result2) > 0):
                break
            if i[j].isnumeric() and len(str_result1) == 0:
                str_result1 += i[j]
            if (i[back_pointer].isnumeric() and len(str_result2) == 0):
                str_result2 += i[back_pointer]
            back_pointer -= 1
        if len(str_result1) == 0:
            str_result = str_result2 + str_result2
        elif len(str_result2) == 0:
            str_result = str_result1 + str_result1
        else:
            str_result = str_result1 + str_result2

        if (len(str_result) == 2):
            result.append(int(str_result))

    print(sum(result))


def second():
    inp = open("adventofcode2023\day1\input.txt",
               "r").read().rstrip().split("\n")
    mapping = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    result = 0

    for i in inp:
        i_len = len(i)
        back_pointer = i_len - 1
        str_result1 = ""
        str_result2 = ""

        for j in range(i_len):
            if (i[j].isnumeric()) and len(str_result1) == 0:
                str_result1 += i[j]
            if (i[back_pointer].isnumeric() and len(str_result2) == 0):
                str_result2 += i[back_pointer]

            if (len(str_result1) > 0 and len(str_result2) > 0):
                break

            for m in mapping:
                if (i[j::].startswith(m) and len(str_result1) == 0):
                    str_result1 += str(mapping[m])
                if (i[:back_pointer + 1].endswith(m) and len(str_result2) == 0):
                    str_result2 += str(mapping[m])

            back_pointer -= 1

        if len(str_result1) == 0:
            str_result = str_result2 + str_result2
            result += int(str_result)
        elif len(str_result2) == 0:
            str_result = str_result1 + str_result1
            result += int(str_result)
        else:
            str_result = str_result1 + str_result2
            result += int(str_result)

    print(result)


second()
