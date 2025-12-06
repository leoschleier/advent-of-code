"""AOC 2025 day 4 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 4 part 2."""
    data = read_input().split("\n")[:-1]
    answer = solve(data)
    print(f"Answer: {answer}")


def solve(data: list[str]) -> int:
    """Solve puzzle."""
    if not data:
        return 0

    movable_threshold = 4
    column_len = len(data)
    row_len = len(data[0])
    initial_rolls = [
        (r, c)
        for r in range(row_len)
        for c in range(column_len)
        if data[r][c] == "@"
    ]

    rolls = set(initial_rolls)
    candidates = set(initial_rolls)
    accessible: set[tuple[int, int]] = set()
    column_len = len(data)
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
                if data[r][c] == "@":
                    n_ajdacent_rolls += 1
            if n_ajdacent_rolls < movable_threshold:
                row = data[row_idx]
                data[row_idx] = row[:column_idx] + "x" + row[column_idx + 1 :]
                accessible.add(this_roll)
                new_candidates |= adjacent & rolls

        visualize(data, title=f"Iteration {iteration}:")
        candidates = new_candidates - accessible
        iteration += 1

    return len(accessible)


def visualize(data: list[str], title: str = "") -> None:
    """Visualize rolls."""
    if title:
        print(title)
    for row in data:
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
