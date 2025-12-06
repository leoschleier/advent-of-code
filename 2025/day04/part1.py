# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 3 part 1."""
    input = read_input().split("\n")[:-1]
    answer = solve(input)
    print(f"Answer: {answer}")


def solve(input: list[str]) -> int:
    """Solve puzzle."""
    n_accessible = 0
    column_len = len(input)
    for row_idx in range(column_len):
        row = input[row_idx]
        row_len = len(row)
        for column_idx in range(row_len):
            item = row[column_idx]
            if item == "@":
                above = max(row_idx - 1, 0)
                below = min(row_idx + 1, column_len - 1)
                left = max(column_idx - 1, 0)
                right = min(column_idx + 1, row_len - 1)
                adjacent = set(
                    (r, c)
                    for r in range(above, below + 1)
                    for c in range(left, right + 1)
                ) - set([(row_idx, column_idx)])
                n_ajdacent_rolls = 0
                for r, c in adjacent:
                    if input[r][c] == "@":
                        n_ajdacent_rolls += 1
                if n_ajdacent_rolls < 4:
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

    with open(file_path, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
