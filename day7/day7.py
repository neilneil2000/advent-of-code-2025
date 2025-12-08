from day7_input import input_data as input_data

SPLITTER = "^"
START = "S"


def process_data():
    manifold = input_data.splitlines()
    splitters = set()
    for y, row in enumerate(manifold):
        for x, location in enumerate(row):
            if location == SPLITTER:
                splitters.add((x, y))
            if location == START:
                start = (x, y)
    return start, splitters


def get_splitter_hit_by_beam(
    splitters: dict[int : set[int]], beam: tuple[int, int]
) -> set:
    """Return location of splitter that would be hit by a given beam"""
    x, y = beam
    possibles = list(filter(lambda a: a > y, splitters.get(x, set())))
    if not possibles:
        return set()
    return {(x, min(possibles))}


def get_beams_from_splitter(x: int, y: int) -> set:
    return {(x - 1, y), (x + 1, y)}


def split_beam(splitters, beams, beam) -> None:
    splitter = get_splitter_hit_by_beam(splitters, beam)
    if not splitter:
        return
    new_beams = get_beams_from_splitter(*splitter.pop())
    for new_beam in new_beams:
        beams[new_beam] = beams.get(new_beam, 0) + beams[beam]
    del beams[beam]


def main():
    start, splitters = process_data()
    s_dict = {}
    for x, y in splitters:
        s_dict[x] = s_dict.get(x, set()) | {y}

    beams = {start}
    active_splits = set()
    while beams:
        new_splits = {s for b in beams for s in get_splitter_hit_by_beam(s_dict, b)}
        active_splits |= new_splits
        beams = {b for s in new_splits for b in get_beams_from_splitter(*s)}

    print(f"Part 1: {len(active_splits)}")

    beams = {start: 1}
    while True:
        start_beams = beams.copy()
        for beam in start_beams:
            split_beam(s_dict, beams, beam)
        if beams == start_beams:
            break

    print(f"Part 2: {sum(beams.values())}")


if __name__ == "__main__":
    main()
