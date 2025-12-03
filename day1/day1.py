from day1_input import input_data as input_data


POSITIONS = 100


def main():
    directions = list(map(lambda x: [x[0], int(x[1:])], input_data.splitlines()))

    # Part 1
    dial = 50
    zeroes = 0
    for direction, steps in directions:
        if direction == "R":
            dial = (dial + steps) % POSITIONS
        else:
            dial = (dial - steps) % POSITIONS
        if not dial:
            zeroes += 1

    print(f"Part 1 Answer: {zeroes}")

    # Part 2
    dial = 50
    zeroes = 0
    for direction, steps in directions:
        if direction == "R":
            zeroes += (dial + steps) // POSITIONS
            dial = (dial + steps) % POSITIONS
        else:
            zero_passes = (dial - steps) // POSITIONS
            if dial == 0:
                zero_passes += 1
            dial = (dial - steps) % POSITIONS
            if dial == 0:
                zero_passes -= 1
            zeroes -= zero_passes

    print(f"Part 2 Answer: {zeroes}")


if __name__ == "__main__":
    main()
