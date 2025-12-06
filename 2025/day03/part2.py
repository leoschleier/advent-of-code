"""AOC 2025 day 3 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 3 part 2."""
    data = read_input()
    input_split = data.split("\n")
    input_int = [[int(s) for s in line] for line in input_split if line]
    answer = solve(input_int)
    print(f"Answer: {answer}")


def solve(data: list[list[int]]) -> int:
    """Solve puzzle."""
    n_digits = 12
    total_joltage = 0
    for bank_number, bank in enumerate(data, start=1):
        n_batteries = len(bank)
        joltage = 0
        search_start, search_stop = (0, n_batteries - n_digits + 1)
        for d in reversed(range(n_digits)):
            search_space = bank[search_start:search_stop]
            digit = max(search_space)
            joltage += digit * 10**d
            digit_idx = search_space.index(digit) + search_start
            search_start = digit_idx + 1
            search_stop = n_batteries - d + 1

        print(f"Bank {bank_number} - joltage={joltage}")

        total_joltage += joltage

    return total_joltage


def read_input() -> str:
    """Load input data from file."""
    file_path = (
        Path() / "input_demo.txt"
        if os.environ.get("AOC_DEMO")
        else Path() / "input.txt"
    )

    with file_path.open() as f:
        return f.read()


if __name__ == "__main__":
    main()
