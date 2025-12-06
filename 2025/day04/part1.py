"""AOC 2025 day 4 part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 4 part 1."""
    data = read_input().split("\n")[:-1]
    answer = solve(data)
    print(f"Answer: {answer}")


def solve(data: list[str]) -> int:
    """Solve puzzle."""
    movable_threshold = 4
    n_accessible = 0
    column_len = len(data)
    for row_idx in range(column_len):
        row = data[row_idx]
        row_len = len(row)
        for column_idx in range(row_len):
            item = row[column_idx]
            if item == "@":
                above = max(row_idx - 1, 0)
                below = min(row_idx + 1, column_len - 1)
                left = max(column_idx - 1, 0)
                right = min(column_idx + 1, row_len - 1)
                adjacent = {
                    (r, c)
                    for r in range(above, below + 1)
                    for c in range(left, right + 1)
                } - {(row_idx, column_idx)}
                n_ajdacent_rolls = 0
                for r, c in adjacent:
                    if data[r][c] == "@":
                        n_ajdacent_rolls += 1
                if n_ajdacent_rolls < movable_threshold:
                    print(f"{(row_idx, column_idx)} accessible")
                    n_accessible += 1

    return n_accessible


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
