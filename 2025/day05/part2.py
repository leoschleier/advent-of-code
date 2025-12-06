"""AOC 2025 day 5 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from pathlib import Path


def main() -> None:
    """Solve day 5 part 2."""
    data = read_input().split("\n\n")

    fresh_id_ranges: list[tuple[int, int]] = []
    for r in data[0].split("\n"):
        s, e = r.split("-")
        fresh_id_ranges.append((int(s), int(e) + 1))

    answer = solve(fresh_id_ranges)
    print(f"Answer: {answer}")


def solve(fresh_id_ranges: list[tuple[int, int]]) -> int:
    """Solve puzzle."""
    unique_ranges: list[tuple[int, int]] = []
    for fresh_range in fresh_id_ranges:
        unique_ranges += find_unique_ranges(fresh_range, unique_ranges)

    return sum(end - start for start, end in unique_ranges)


def find_unique_ranges(
    fresh: tuple[int, int], processed: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Find unique ranges in fresh given processed."""
    unique: list[tuple[int, int]] = []
    r_start, r_end = fresh
    for i, (p_start, p_end) in enumerate(processed):
        if p_start <= r_start <= r_end <= p_end:
            # New range fully contained in processed range
            break
        if r_start <= p_start <= p_end <= r_end:
            # Processed range fully contained in new range
            offset = max(i - 1, 0)
            unique += find_unique_ranges(
                (r_start, p_start), processed[offset:]
            )
            unique += find_unique_ranges((p_end, r_end), processed[offset:])
            break

        # Reduce range by processed range
        if p_start <= r_start <= p_end:
            r_start = min(p_end, r_end)
        elif p_start <= r_end <= p_end:
            r_end = max(p_start, r_start)
    else:
        unique.append((r_start, r_end))

    return unique


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
