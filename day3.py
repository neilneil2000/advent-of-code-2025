from day3_input import input_data as input_data


def get_joltage(units):
    """Closure to return joltage calculator for fixed length"""

    def max_joltage(bank: str) -> int:
        """Return max [units] digit number without rearranging digits"""
        enabled_batteries = []
        for i in range(units - 1, 0, -1):
            enabled_batteries.append(max(bank[:-i]))
            bank = bank[bank.find(enabled_batteries[-1]) + 1 :]
        enabled_batteries.append(max(bank))
        return int("".join(enabled_batteries))

    return max_joltage


def main():
    banks = input_data.splitlines()
    joltage = sum(map(get_joltage(2), banks))
    print(f"Part 1: {joltage}")

    joltage = sum(map(get_joltage(12), banks))
    print(f"Part 2: {joltage}")


if __name__ == "__main__":
    main()
