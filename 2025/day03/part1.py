"""AOC 2025 day 3 part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 3 part 1."""
    data = read_input()
    input_split = data.split("\n")
    input_int = [[int(s) for s in line] for line in input_split if line]
    answer = solve(input_int)
    print(f"Answer: {answer}")


def solve(data: list[list[int]]) -> int:
    """Solve puzzle."""
    total_joltage = 0
    for bank_number, bank in enumerate(data, start=1):
        left_digit = max(bank[:-1])
        left_idx = bank.index(left_digit)
        right_digit = max(bank[left_idx + 1 :])
        joltage = left_digit * 10 + right_digit

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
