import re


def parse_input_gives(input_str):
    match = re.match(
        r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", input_str)

    if match:
        return int(match.group(1)), (match.group(2), int(match.group(3))), (match.group(4), int(match.group(5)))

    return None


def parse_input_value(input_str):
    match = re.match(r"value (\d+) goes to bot (\d+)", input_str)
    if match:
        value = int(match.group(1))
        bot_number = int(match.group(2))

        return value, bot_number

    return None


def part1():
    data = open("input.txt").read().strip().split("\n")

    instructions = {}

    for line in data:
        if "gives" in line:
            bot_number, low, high = parse_input_gives(line)
            instructions[bot_number] = [low, high]

    bots = {}
    outputs = {}
    stack = []

    for line in data:
        if "value" in line:
            value, bot_number = parse_input_value(line)

            if bot_number not in bots:
                bots[bot_number] = []

            bots[bot_number].append(value)

            if len(bots[bot_number]) == 2:
                stack.append(bot_number)

    while stack:
        bot_number = stack.pop()

        low, high = instructions[bot_number]

        low_type, low_number = low
        high_type, high_number = high

        low_value, high_value = sorted(bots[bot_number])

        if low_value == 17 and high_value == 61:
            print("Part 1:", bot_number)

        if low_type == "bot":
            if low_number not in bots:
                bots[low_number] = []

            bots[low_number].append(low_value)

            if len(bots[low_number]) == 2:
                stack.append(low_number)

        else:
            if low_number not in outputs:
                outputs[low_number] = []

            outputs[low_number].append(low_value)

        if high_type == "bot":
            if high_number not in bots:
                bots[high_number] = []

            bots[high_number].append(high_value)

            if len(bots[high_number]) == 2:
                stack.append(high_number)

        else:
            if high_number not in outputs:
                outputs[high_number] = []

            outputs[high_number].append(high_value)

    print("Part 2:", outputs[0][0] * outputs[1][0] * outputs[2][0])


part1()
