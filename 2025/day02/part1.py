# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 2 part 1."""
    input = read_input()
    input_split = input.split(",")
    id_ranges: list[tuple[int, int]] = []
    for id_range in input_split:
        r = id_range.split("-")
        id_ranges.append((int(r[0]), int(r[1])))

    answer = solve(id_ranges)
    print(f"Answer: {answer}")


def solve(id_ranges: list[tuple[int, int]]) -> int:
    """Solve puzzle."""
    invalid_sum = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if is_invalid(str(id)):
                print(f"Invalid ID: {id}")
                invalid_sum += id
    return invalid_sum


def is_invalid(id: str) -> bool:
    """Check whether a given ID is invalid.

    An ID is invalid if only made of some sequence of digits repeated
    twice.
    """
    id_len = len(id)
    if id_len % 2 != 0:
        return False

    mid = id_len // 2

    for i in range(0, mid):
        if id[i] != id[i + mid]:
            return False

    return True


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
