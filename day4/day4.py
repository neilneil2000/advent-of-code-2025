from day4_input import input_data as input_data


def number_of_neighbours(location: tuple[int, int], population: set) -> int:
    """Returns number of adjacent cells (including diagonals are in population set)"""
    x, y = location
    neighbours = {
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    }
    return len(neighbours & population)


def get_locations_in_grid(match_value: str, grid: str) -> set[tuple[int, int]]:
    """Return set of (x,y) locations where value is match_value in multiline string 'grid'"""
    w = grid.find("\n")
    data = "".join(input_data.splitlines())
    return {(i % w, i // w) for i, c in enumerate(data) if c == match_value}


def main():
    PAPER = "@"
    paper = get_locations_in_grid(PAPER, input_data)
    accessible = {loc for loc in paper if number_of_neighbours(loc, paper) < 4}
    print(len(accessible))


if __name__ == "__main__":
    main()
