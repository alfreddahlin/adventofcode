import os


def get_input(file, delimiter="\n"):
    year_folder = os.path.dirname(file)
    problem_file_name = os.path.basename(file)

    ïnput_file = f"{year_folder}/inputs/{problem_file_name.replace('.py', '.in')}"

    return open(ïnput_file, "r").read().strip().split(delimiter)
