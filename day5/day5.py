from day5_input import input_data as input_data


def process_data() -> tuple:
    """Process Input Data"""
    my_data = list(map(str.splitlines, input_data.split("\n\n")))
    ingredients = list(map(int, my_data[1]))
    ingredient_ranges = []
    for entry in my_data[0]:
        start, end = entry.split("-")
        ingredient_ranges.append((int(start), int(end)))
    return ingredient_ranges, ingredients


def in_a_range(value: int, ranges: list) -> bool:
    """Returns True is value is in at least one range"""
    for low, high in ranges:
        if low <= value <= high:
            return True
    return False


def collapse_inclusive_ranges(*args: tuple[int, int]) -> tuple[int, int]:
    """Returns a tuple representing the combined range input ranges"""
    lows, highs = tuple(zip(*args))
    return min(lows), max(highs)


def does_overlap(range_a, range_b) -> bool:
    """Returns true if two inclusive ranges overlap"""
    lows, highs = tuple(zip(range_a, range_b))
    return min(highs) + 1 >= max(lows)


def consolidate_ranges(ranges) -> set:
    """Reduce ranges to non-overlapping set"""
    consolidated = set()
    for r in ranges:
        overlaps = set(filter(lambda x: does_overlap(r, x), consolidated))
        if len(overlaps) == 0:
            consolidated.add(r)
        else:
            consolidated -= overlaps
            consolidated |= {collapse_inclusive_ranges(*overlaps, r)}
    return consolidated


def main():
    ingredient_ranges, ingredients = process_data()

    part_1 = sum(in_a_range(i, ingredient_ranges) for i in ingredients)
    print(f"Part 1: {part_1}")

    part_2 = sum(map(lambda x: x[1] - x[0] + 1, consolidate_ranges(ingredient_ranges)))
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
