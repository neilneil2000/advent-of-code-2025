from day9_input import input_data as input_data


def get_area(a, b):
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1
    return x * y


def process_input():
    return list(
        map(
            lambda x: (int(x[0]), int(x[1])),
            map(lambda x: x.split(","), input_data.splitlines()),
        )
    )


def get_rectangle_lines(a, b):
    """Return edge lines of rectangle given opposite corners"""
    ax, ay = a
    bx, by = b
    if ax == bx or ay == by:
        return [(a, b)]
    return [(a, (bx, ay)), (a, (ax, by)), (b, (bx, ay)), (b, (ax, by))]


def is_rectangle_internal_to_polygon(a, b, lines):
    ax, ay = a
    bx, by = b
    if ax == bx or ay == by:  # i.e. it's a single line
        return (a, b) in lines or (b, a) in lines
    test_points = [
        (min(ax, bx) + 0.5, min(ay, by) + 0.5),
        (min(ax, bx) + 0.5, max(ay, by) - 0.5),
        (max(ax, bx) - 0.5, min(ay, by) + 0.5),
        (max(ax, bx) - 0.5, max(ay, by) - 0.5),
    ]
    for test_point in test_points:
        if not is_point_internal_to_polygon(test_point, lines):
            return False
    return True


def is_point_internal_to_polygon(point, lines):
    """Uses Ray Casting to determine whether a point is within a polygon"""
    # Need to consider the odd cases of thin rectangles
    px, py = point  # Fix y axis and look out to the right
    cross_counter = 0
    for a, b in lines:
        ax, ay = a
        bx, by = b
        if ay == by:
            continue  # Ignore parallel lines
        if min(ay, by) < py < max(ay, by) and ax > px:  # we know ax==bx
            cross_counter += 1
    return bool(cross_counter % 2)


def lines_cross(a: tuple[tuple[int, int]], b: tuple[tuple[int, int]]):
    """Returns true if lines cross"""
    a_1, a_2 = a
    b_1, b_2 = b
    a_1x, a_1y = a_1
    a_2x, a_2y = a_2
    b_1x, b_1y = b_1
    b_2x, b_2y = b_2
    if a_1x == a_2x and b_1x == b_2x:
        return False  # Parallel Vertical
    if a_1y == a_2y and b_1y == b_2y:
        return False  # Parallel Horizontal
    if min(a_1x, a_2x) >= max(b_1x, b_2x) or min(b_1x, b_2x) >= max(a_1x, a_2x):  #  -|
        return False
    if min(a_1y, a_2y) >= max(b_1y, b_2y) or min(b_1y, b_2y) >= max(a_1y, a_2y):  #  T
        return False
    if a_1x == a_2x and min(b_1x, b_2x) < a_1x < max(b_1x, b_2x):
        return True
    if b_1x == b_2x and min(a_1x, a_2x) < b_1x < max(a_1x, a_2x):
        return True
    return False


def any_crossing_lines(check_lines, all_lines):
    """Returns True if any line in all_lines crosses a check line"""
    for line in all_lines:
        for check_line in check_lines:
            if lines_cross(line, check_line):
                return True
    return False


def main():
    corners = process_input()

    best = 0
    for i, a in enumerate(corners):
        for b in corners[i + 1 :]:
            best = max(best, get_area(a, b))
    print(f"Part 1: {best}")

    lines = [(corners[i - 1], corners[i]) for i, _ in enumerate(corners)]

    best = 0
    for i, a in enumerate(corners):
        for b in corners[i + 1 :]:
            area = get_area(a, b)
            if area <= best:
                continue
            if not is_rectangle_internal_to_polygon(a, b, lines):
                continue  # check it is an inside rectangle
            if any_crossing_lines(
                get_rectangle_lines(a, b), lines
            ):  # check for crossing lines
                continue
            best = area

    print(f"Part 2: {best}")


if __name__ == "__main__":
    main()
