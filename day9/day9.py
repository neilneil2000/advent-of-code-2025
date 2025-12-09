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


def main():
    corners = process_input()
    best = 0
    for i, a in enumerate(corners):
        for b in corners[i:]:
            best = max(best, get_area(a, b))
    print(f"Part 1: {best}")


if __name__ == "__main__":
    main()
