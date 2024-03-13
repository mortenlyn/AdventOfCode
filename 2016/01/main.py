# Part 1

# with open("input.txt", "r") as f:
#     info = f.read().strip().split(", ")
#     direction = "N"
#     blocks_up = 0
#     blocks_left = 0


#     for i in info:
#         if i[0] == "L":
#             if direction == "N":
#                 direction = "W"
#                 blocks_left += int(i[1::])

#             elif direction == "W":
#                 direction = "S"
#                 blocks_up -= int(i[1::])

#             elif direction == "S":
#                 direction = "E"
#                 blocks_left -= int(i[1::])

#             elif direction == "E":
#                 direction = "N"
#                 blocks_up += int(i[1::])

#         if i[0] == "R":
#             if direction == "N":
#                 direction = "E"
#                 blocks_left -= int(i[1::])


#             elif direction == "E":
#                 direction = "S"
#                 blocks_up -= int(i[1::])


#             elif direction == "S":
#                 direction = "W"
#                 blocks_left += int(i[1::])


#             elif direction == "W":
#                 direction = "N"
#                 blocks_up += int(i[1::])


#     print("Part 1: ", abs(blocks_up) + abs(blocks_left))


# Part 2:

visited = []

with open("input.txt", "r") as f:
    info = f.read().strip().split(", ")
    direction = "N"
    blocks_up = 0
    blocks_left = 0
    visited = []

    for i in info:
        distance = int(i[1::])

        if i[0] == "L":
            if direction == "N":
                direction = "W"
                for _ in range(distance):
                    blocks_left += 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "W":
                direction = "S"
                for _ in range(distance):
                    blocks_up -= 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "S":
                direction = "E"
                for _ in range(distance):
                    blocks_left -= 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "E":
                direction = "N"
                for _ in range(distance):
                    blocks_up += 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

        elif i[0] == "R":
            if direction == "N":
                direction = "E"
                for _ in range(distance):
                    blocks_left -= 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "E":
                direction = "S"
                for _ in range(distance):
                    blocks_up -= 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "S":
                direction = "W"
                for _ in range(distance):
                    blocks_left += 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))

            elif direction == "W":
                direction = "N"
                for _ in range(distance):
                    blocks_up += 1
                    if (blocks_up, blocks_left) in visited:
                        print("Part 2: ", abs(blocks_left) + abs(blocks_up))
                        exit()
                    visited.append((blocks_up, blocks_left))
