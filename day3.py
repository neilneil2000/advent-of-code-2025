from day3_input import input_data as input_data


def max_joltage(bank: str) -> int:
    """Return max two digit number without rearranging digits"""
    left = max(bank[:-1])
    right = max(bank[bank.find(left) + 1 :])
    return int(left + right)


def max_joltage_12(bank: str) -> int:
    """Return max 12 digit number without rearranging digits"""
    enabled_batteries = []
    for i in range(11, 0, -1):
        enabled_batteries.append(max(bank[:-i]))
        bank = bank[bank.find(enabled_batteries[-1]) + 1 :]
    enabled_batteries.append(max(bank))
    return int("".join(enabled_batteries))


def main():
    banks = input_data.splitlines()
    joltage = sum(map(max_joltage, banks))
    print(f"Part 1: {joltage}")

    joltage = sum(map(max_joltage_12, banks))
    print(f"Part 2: {joltage}")


if __name__ == "__main__":
    main()
