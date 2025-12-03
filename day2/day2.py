from day2_input import input_data as input_data

import textwrap


def is_valid(value: str) -> bool:
    """Returns False if first and second half of string are equal"""
    if len(value) % 2:
        return True
    return value[: len(value) // 2] != value[len(value) // 2 :]


def is_valid_2(value: str) -> bool:
    """Returns False if string is made up of repeating substrings"""
    for i in range(1, len(value) // 2 + 1):
        if len(value) % i:
            continue
        check = set(textwrap.wrap(value, i))
        if len(check) == 1:
            return False
    return True


def get_invalid_ids(start: int, end: int, check_function: callable) -> list[int]:
    """Return list of invalid IDs"""
    invalid_ids = []
    for value in range(start, end + 1):
        if check_function(str(value)):
            continue
        invalid_ids.append(value)
    return invalid_ids


def main():
    items = list(map(lambda x: x.split("-"), input_data.split(",")))

    total = 0
    for start, end in items:
        total += sum(get_invalid_ids(int(start), int(end), is_valid))
    print(total)

    total = 0
    for start, end in items:
        total += sum(get_invalid_ids(int(start), int(end), is_valid_2))
    print(total)


if __name__ == "__main__":
    main()
