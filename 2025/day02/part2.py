"""AOC 2025, day 2, part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 2 part 2."""
    data = read_input()
    input_split = data.split(",")
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
        for id_ in range(start, end + 1):
            if is_invalid(str(id)):
                print(f"Invalid ID: {id_}")
                invalid_sum += id_
    return invalid_sum


def is_invalid(id_: str) -> bool:
    """Check whether a given ID is invalid.

    An ID is invalid if only made of some sequence of digits repeated
    at least twice.
    """
    id_len = len(id_)
    if id_len < 2:  # noqa: PLR2004
        return False

    is_invalid = True
    for pattern_length in range(1, id_len):
        if id_len % pattern_length != 0:
            continue

        is_invalid = True
        ref = id_[:pattern_length]
        for i in range(pattern_length, id_len, pattern_length):
            if ref != id_[i : i + pattern_length]:
                is_invalid = False
                break

        if is_invalid:
            break

    return is_invalid


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
