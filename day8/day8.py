import math

from day8_input import input_data as input_data


def offset(a, b):
    a = tuple(map(int, a))
    b = tuple(map(int, b))
    return abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])


def process_data():
    boxes = list(map(lambda x: x.split(","), input_data.splitlines()))
    box_dict = {}
    for i, a in enumerate(boxes):
        for j, b in enumerate(boxes[i + 1 :]):
            dist = math.hypot(*offset(a, b))
            if dist in box_dict:
                raise ValueError("Duplicate Value")
            box_dict[dist] = (i, j + i + 1)
    return boxes, box_dict


def connect_boxes(box_dict, circuits, limit=-1):
    """Connect Boxes up to maximum number set by limit"""
    x = 0
    for _, v in sorted(box_dict.items()):
        if x == limit:
            break
        x += 1
        if len(circuits) == 1:
            break
        a, b = v
        for i, circuit in enumerate(circuits):
            if a in circuit:
                set_a = i
            if b in circuit:
                set_b = i
        if set_a != set_b:
            circuits[set_a] |= circuits[set_b]
            circuits.pop(set_b)
    return a, b


def main():
    boxes, box_dict = process_data()
    circuits = [{i} for i in range(len(boxes))]
    connect_boxes(box_dict, circuits, 1000)

    lengths = [len(circuit) for circuit in circuits]
    part_1 = math.prod(sorted(lengths, reverse=True)[:3])
    print(f"Part 1: {part_1}")

    a, b = connect_boxes(box_dict, circuits)
    part_2 = int(boxes[a][0]) * int(boxes[b][0])
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
