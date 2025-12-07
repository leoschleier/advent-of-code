"""AOC 2025 day 6 part 1."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from functools import reduce
from operator import add, mul
from pathlib import Path


def main() -> None:
    """Solve day 6 part 1."""
    raw = read_input()
    numbers, operators = parse_inputs(raw)

    answer = solve(numbers, operators)
    print(f"Answer: {answer}")


def parse_inputs(raw: str) -> tuple[list[list[int]], list[str]]:
    """Parse raw inputs into numbers and operations."""
    data = raw.split("\n")[:-1]
    problems = [[n] for n in data[0].strip().split(" ") if n]
    for row in data[1:]:
        row_split = row.split(" ")
        p_idx = 0
        for n in row_split:
            if n:
                problems[p_idx].append(n)
                p_idx += 1

    numbers: list[list[int]] = []
    operators: list[str] = []
    for problem in problems:
        nums = [int(n) for n in problem[:-1]]
        numbers.append(nums)
        operators.append(problem[-1])

    return numbers, operators


def solve(numbers: list[list[int]], operators: list[str]) -> int:
    """Solve puzzle."""
    py_ops = {
        "+": add,
        "*": mul,
    }

    result = 0
    for nums, op in zip(numbers, operators, strict=True):
        r = reduce(py_ops[op], nums)
        print(f"numbers={nums}, operator={op}, result={r}")
        result += r

    return result


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
