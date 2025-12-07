import math

from day6_input import input_data as input_data


def chunk_numbers_into_problems(numbers):
    problems = []
    current = []
    for number in numbers:
        if not all(x == " " for x in number):
            current.append(number)
        else:
            problems.append(current)
            current = []
    else:
        problems.append(current)
    return problems


def cephalopod_maths(numbers, operator) -> int:
    operator = sum if operator == ["+"] else math.prod
    numbers = filter(lambda x: not all(y == " " for y in x), numbers)
    values = [int("".join(number)) for number in numbers]
    return operator(values)


def main():
    part_1 = 0
    for problem in zip(*map(str.split, input_data.splitlines())):
        operator = sum if problem[-1] == "+" else math.prod
        part_1 += operator(map(int, problem[:-1]))
    print(f"Part 1: {part_1}")

    numbers = list(zip(*input_data.splitlines()[:-1]))
    problems = chunk_numbers_into_problems(numbers)
    operators = list(filter(bool, map(str.split, input_data.splitlines()[-1])))
    part_2 = sum(cephalopod_maths(*problem) for problem in zip(problems, operators))
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
