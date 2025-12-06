"""AOC 2025 day 3 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 3 part 2."""
    input = read_input().split("\n")[:-1]
    answer = solve(input)
    print(f"Answer: {answer}")


def solve(input: list[str]) -> int:
    """Solve puzzle."""
    if not input:
        return 0

    movable_threshold = 4
    column_len = len(input)
    row_len = len(input[0])
    initial_rolls = [
        (r, c)
        for r in range(row_len)
        for c in range(column_len)
        if input[r][c] == "@"
    ]

    rolls = set(initial_rolls)
    candidates = set(initial_rolls)
    accessible: set[tuple[int, int]] = set()
    column_len = len(input)
    iteration = 0
    while candidates:
        new_candidates: set[tuple[int, int]] = set()
        for row_idx, column_idx in candidates:
            this_roll = (row_idx, column_idx)
            above = max(row_idx - 1, 0)
            below = min(row_idx + 1, column_len - 1)
            left = max(column_idx - 1, 0)
            right = min(column_idx + 1, row_len - 1)
            adjacent = {
                (r, c)
                for r in range(above, below + 1)
                for c in range(left, right + 1)
            }
            adjacent.remove(this_roll)
            n_ajdacent_rolls = 0
            for r, c in adjacent:
                if input[r][c] == "@":
                    n_ajdacent_rolls += 1
            if n_ajdacent_rolls < movable_threshold:
                row = input[row_idx]
                input[row_idx] = row[:column_idx] + "x" + row[column_idx + 1 :]
                accessible.add(this_roll)
                new_candidates |= adjacent & rolls

        visualize(input, title=f"Iteration {iteration}:")
        candidates = new_candidates - accessible
        iteration += 1

    return len(accessible)


def visualize(input: list[str], title: str = "") -> None:
    """Visualize rolls."""
    if title:
        print(title)
    for row in input:
        print(row)
    print()


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
