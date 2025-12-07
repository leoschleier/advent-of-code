"""AOC 2025 day 6 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import os
from functools import reduce
from operator import add, mul
from pathlib import Path


def main() -> None:
    """Solve day 6 part 2."""
    raw = read_input()
    numbers, operators = parse_inputs(raw)

    answer = solve(numbers, operators)
    print(f"Answer: {answer}")


def parse_inputs(raw: str) -> tuple[list[list[int]], list[str]]:
    """Parse raw inputs into numbers and operations."""
    data = raw.split("\n")[:-1]

    num_lengths: list[int] = []
    operators_raw = data[-1].split(" ")
    operators: list[str] = []
    op_idx = -1
    for operator in operators_raw:
        if operator:
            operators.append(operator)
            num_lengths.append(1)
            op_idx += 1
        else:
            num_lengths[op_idx] += 1

    numbers: list[list[int]] = []
    offset = 0
    for nl in num_lengths:
        nums = []
        for i in reversed(range(nl)):
            number = ""
            idx = offset + i
            for row in data[:-1]:
                digit = row[idx]
                number += digit if digit else "0"
            nums.append(int(number))
        numbers.append(nums)
        offset += nl + 1

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
