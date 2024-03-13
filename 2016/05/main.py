import hashlib


def part1():
    data = open("input.txt", "r").read().strip()

    s = ""
    counter = 0

    while True:
        counter += 1
        hash_object = hashlib.md5((data + str(counter)).encode())

        if hash_object.hexdigest().startswith("00000"):
            s += str(hash_object.hexdigest())[5]

            if len(s) == 8:
                print(s)
                break


# part1()


def part2():
    data = open("input.txt", "r").read().strip()

    s = [None, None, None, None, None, None, None, None]
    counter = 0

    while True:
        counter += 1
        hash_object = hashlib.md5((data + str(counter)).encode())
        if hash_object.hexdigest().startswith("00000"):
            if (int((hash_object.hexdigest())[5], 16) > 7):
                continue

            if s[int((hash_object.hexdigest())[5], 16)] == None:
                s[int((hash_object.hexdigest())[5], 16)] = str(
                    hash_object.hexdigest())[6]

            if None not in s:
                print("".join(s))
                break


part2()
