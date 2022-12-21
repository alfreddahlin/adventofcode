import re

input_data = open("inputs/day21.in", "r").read().strip()
data = re.findall(r"(.*): (.*)", input_data)

monkeys = {i: number.split() for i, number in data}


def yell(monkeys, monkey):
    utterance = monkeys[monkey]
    if len(utterance) == 1:
        return int(utterance[0])
    else:
        match utterance[1]:
            case "+":
                return yell(monkeys, utterance[0]) + yell(monkeys, utterance[2])
            case "-":
                return yell(monkeys, utterance[0]) - yell(monkeys, utterance[2])
            case "*":
                return yell(monkeys, utterance[0]) * yell(monkeys, utterance[2])
            case "/":
                return yell(monkeys, utterance[0]) // yell(monkeys, utterance[2])


def find(monkeys, monkey, value):
    if monkey == "humn":
        return value

    utterance = monkeys[monkey]
    if monkey == "root":
        utterance[1] = "="

    try:
        term = yell(monkeys, utterance[0])
    except TypeError:
        search = 0
    try:
        term = yell(monkeys, utterance[2])
    except TypeError:
        search = 2

    match utterance[1]:
        case "+":
            return find(monkeys, utterance[search], value - term)
        case "-":
            if search == 0:
                return find(monkeys, utterance[search], value + term)
            if search == 2:
                return find(monkeys, utterance[search], term - value)
        case "*":
            return find(monkeys, utterance[search], value // term)
        case "/":
            if search == 0:
                return find(monkeys, utterance[search], value * term)
            if search == 2:
                return find(monkeys, utterance[search], term // value)
        case "=":
            return find(monkeys, utterance[search], term)


print("Part 1:", yell(monkeys, "root"))

monkeys["humn"] = None
print("Part 2:", find(monkeys, "root", None))
