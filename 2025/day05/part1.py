"""AOC 2025 day 5 part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 5 part 1."""
    data = read_input().split("\n\n")

    fresh_id_ranges: list[tuple[int, int]] = []
    for r in data[0].split("\n"):
        s, e = r.split("-")
        fresh_id_ranges.append((int(s), int(e)))
    available_ids: list[int] = [int(d) for d in data[1].split("\n")[:-1]]

    answer = solve(fresh_id_ranges, available_ids)
    print(f"Answer: {answer}")


def solve(
    fresh_id_ranges: list[tuple[int, int]], available_ids: list[int]
) -> int:
    """Solve puzzle."""
    n_fresh_available = 0
    for available_id in available_ids:
        for fresh_id_min, fresh_id_max in fresh_id_ranges:
            if fresh_id_min <= available_id <= fresh_id_max:
                n_fresh_available += 1
                break

    return n_fresh_available


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
