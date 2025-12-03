from day2_input import input_data as input_data


def is_valid(value: str) -> bool:
    """Returns False if first and second half of string are equal"""
    if len(value) % 2:
        return True
    return value[: len(value) // 2] != value[len(value) // 2 :]


def is_valid_2(value: str) -> bool:
    """Returns False if string is made up of repeating substrings"""
    if len(value) % 2:
        return True
    return value[: len(value) // 2] != value[len(value) // 2 :]


def get_invalid_ids(start: int, end: int) -> list[int]:
    """Return list of invalid IDs"""
    invalid_ids = []
    for value in range(start, end + 1):
        if is_valid(str(value)):
            continue
        invalid_ids.append(value)
    return invalid_ids


def main():
    items = list(map(lambda x: x.split("-"), input_data.split(",")))
    total = 0
    for start, end in items:
        total += sum(get_invalid_ids(int(start), int(end)))
    print(total)


if __name__ == "__main__":
    main()
