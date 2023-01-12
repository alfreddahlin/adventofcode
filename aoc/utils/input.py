import os
import re


def get_input(file, delimiter=None):
    year_folder = os.path.dirname(file)
    problem_file_name = os.path.basename(file)

    input_file = f"{year_folder}/inputs/{problem_file_name.replace('.py', '.in')}"
    data = open(input_file, "r").read().strip()
    if delimiter:
        return data.split(delimiter)
    else:
        return data


def get_string_numbers(input):
    found = re.findall(r"-?\d+", input)
    return mapl(int, found)


def get_numbers(file):
    return get_string_numbers(get_input(file))


def get_line_numbers(file):
    lines = get_input(file, "\n")
    return [get_numbers(line) for line in lines]


def mapl(func, iter):
    return list(map(func, iter))


def mapt(func, iter):
    return tuple(map(func, iter))
