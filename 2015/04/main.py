import hashlib


def part1():
    data = open("input.txt", "r").read().strip()

    counter = 0
    while True:
        counter += 1
        hash_object = hashlib.md5((data + str(counter)).encode())
        if hash_object.hexdigest().startswith("000000"):
            print(counter)
            break


part1()
