from day5_input import input_data as input_data


def process_data():
    my_data = list(map(str.splitlines, input_data.split("\n\n")))
    ingredients = list(map(int, my_data[1]))
    ingredient_ranges = []
    for entry in my_data[0]:
        start, end = entry.split("-")
        ingredient_ranges.append((int(start), int(end)))
    return ingredient_ranges, ingredients


def in_range(value: int, low: int, high: int) -> bool:
    """Returns true if value is within low and high (inclusive)"""
    return low <= value <= high


def in_a_range(value: int, ranges: list):
    """Returns true is value is in at least one range"""
    for my_range in ranges:
        if in_range(value, *my_range):
            return True
    return False


def main():
    ingredient_ranges, ingredients = process_data()
    part_1 = sum(in_a_range(i, ingredient_ranges) for i in ingredients)
    print(f"Part 1: {part_1}")


if __name__ == "__main__":
    main()
