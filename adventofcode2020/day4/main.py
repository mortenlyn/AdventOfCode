import re


def part1():
    data = open("adventofcode2020\day4\input.txt").read().strip().split("\n\n")

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    result = 0

    for line in data:
        flag = True
        for field in fields:
            if field not in line:
                flag = False
                break
        if flag:
            result += 1

    print(result)


# part1()

def checkValidNoRegex(line, fields):
    for field in fields:
        if field not in line:
            return False

    line = line.split(" ")

    for i in range(len(line)):
        line[i] = line[i].split(":")

    for i in line:
        if i[0] == "byr":
            if not (1920 <= int(i[1]) <= 2002):
                return False

        elif i[0] == "iyr":
            if not (2010 <= int(i[1]) <= 2020):
                return False

        elif i[0] == "eyr":
            if not (2020 <= int(i[1]) <= 2030):
                return False

        elif i[0] == "hgt":
            if i[1][-2:] == "cm":
                if not (150 <= int(i[1][:-2]) <= 193):
                    return False
            elif i[1][-2:] == "in":
                if not (59 <= int(i[1][:-2]) <= 76):
                    return False
            else:
                return False

        elif i[0] == "hcl":
            if not (i[1][0] == "#" and len(i[1]) == 7):
                return False

            for j in range(1, len(i[1])):
                if i[1][j] not in "0123456789abcdef":
                    return False

        elif i[0] == "ecl":
            if i[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

        elif i[0] == "pid":
            if not (len(i[1]) == 9 and i[1].isdigit()):
                return False

    return True


def checkValidWithRegex(line, fields):
    for field in fields:
        if field not in line:
            return False

    line = line.split(" ")

    for i in range(len(line)):
        line[i] = line[i].split(":")

    for i in line:
        if i[0] == "byr":
            if not (1920 <= int(i[1]) <= 2002):
                return False

        elif i[0] == "iyr":
            if not (2010 <= int(i[1]) <= 2020):
                return False

        elif i[0] == "eyr":
            if not (2020 <= int(i[1]) <= 2030):
                return False

        elif i[0] == "hgt":
            if i[1][-2:] == "cm":
                if not (150 <= int(i[1][:-2]) <= 193):
                    return False
            elif i[1][-2:] == "in":
                if not (59 <= int(i[1][:-2]) <= 76):
                    return False
            else:
                return False

        elif i[0] == "hcl":
            if not re.match(r"^#[0-9a-f]{6}$", i[1]):
                return False

        elif i[0] == "ecl":
            if i[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

        elif i[0] == "pid":
            if not re.match(r"^[0-9]{9}$", i[1]):
                return False

    return True


def part2():
    data = open("adventofcode2020\day4\input.txt").read().strip().split("\n\n")
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    result = 0

    for line in range(len(data)):
        data[line] = data[line].replace("\n", " ")

    for line in data:
        if checkValidWithRegex(line, fields):
            result += 1

    print(result)


part2()
