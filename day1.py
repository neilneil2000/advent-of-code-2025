from day1_input import input_data


POSITIONS = 100


def main():
    directions = list(map(lambda x: [x[0], int(x[1:])], input_data.splitlines()))
    dial = 50
    zeroes = 0
    for direction, steps in directions:
        if direction == "R":
            dial = (dial + steps) % POSITIONS
        else:
            dial = (dial - steps) % POSITIONS
        if not dial:
            zeroes += 1

    print(zeroes)


if __name__ == "__main__":
    main()
