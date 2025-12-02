# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import os
from pathlib import Path


def main() -> None:
    """Solve day 1, part 1."""
    input = read_input()

    answer = parse(input)

    print(f"Answer: {answer}")


def parse(input: str) -> int:
    """Parse input."""
    input_split = input.split("\n")
    dial = 50
    password = 0
    for line in input_split:
        if not line:
            continue

        direction = line[0]
        sign = -1 if direction == "L" else 1
        number = int(line[1:])
        dial = (dial + sign * number) % 100

        print(f"Rotation: {line} - Dial: {dial}")

        if dial == 0:
            password += 1

    return password


def read_input() -> str:
    """Load input data from file."""
    file_path = (
        Path() / "input_demo.txt"
        if os.environ.get("AOC_DEMO")
        else Path() / "input.txt"
    )

    with open(file_path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
