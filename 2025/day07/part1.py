"""AOC 2025 day 7 part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
import re
from pathlib import Path


def main() -> None:
    """Solve day 7 part 1."""
    lines = read_input().split("\n")[:-1]
    answer = solve(lines)
    print(f"Answer: {answer}")


def solve(lines: list[str]) -> int:
    """Solve puzzle."""
    n_splits = 0
    tpos = find("S", lines[0])
    for line in lines[1:]:
        spos = find(r"\^", line)
        new_tpos = set()
        for tp in tpos:
            if tp in spos:
                n_splits += 1
                new_tpos.add(tp - 1)
                new_tpos.add(tp + 1)
            else:
                new_tpos.add(tp)
        tpos = new_tpos

    return n_splits


def find(sub: str, string: str) -> list[int]:
    """Find all starting indexes of a substring in a given string."""
    return [m.start() for m in re.finditer(sub, string)]


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
