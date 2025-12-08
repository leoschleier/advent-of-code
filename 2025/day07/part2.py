"""AOC 2025 day 7 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
import re
from pathlib import Path


def main() -> None:
    """Solve day 7 part 2."""
    lines = read_input().split("\n")[:-1]
    answer = solve(lines)
    print(f"Answer: {answer}")


def solve(lines: list[str]) -> int:
    """Solve puzzle."""
    if not lines:
        return 0

    paths: dict[int, int] = dict.fromkeys(range(len(lines[0])), 1)
    for line in reversed(lines[1:-1]):
        spos = find(r"\^", line)
        for s in spos:
            paths[s] = paths[s - 1] + paths[s + 1]

    return paths[find("S", lines[0])[0]]


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
