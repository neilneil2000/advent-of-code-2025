import math

from day6_input import input_data as input_data


def main():
    part_1 = 0
    for problem in zip(*map(str.split, input_data.splitlines())):
        operator = sum if problem[-1] == "+" else math.prod
        part_1 += operator(map(int, problem[:-1]))
    print(f"Part 1: {part_1}")


if __name__ == "__main__":
    main()
