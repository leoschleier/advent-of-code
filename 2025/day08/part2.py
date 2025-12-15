"""AOC 2025 day 8 part 2."""

# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import math
import os
from pathlib import Path


def main() -> None:
    """Solve day 8 part 2."""
    raw = read_input()
    positions = parse(raw)

    answer = solve(positions)
    print(f"Answer: {answer}")


def parse(raw: str) -> list[tuple[int, int, int]]:
    """Parse raw inputs."""
    lines = raw.split("\n")[:-1]
    positions = []
    for line in lines:
        l_split = line.split(",")
        positions.append((int(l_split[0]), int(l_split[1]), int(l_split[2])))

    return positions


def solve(positions: list[tuple[int, int, int]]) -> int:
    """Solve puzzle."""
    distances: dict[
        tuple[tuple[int, int, int], tuple[int, int, int]], float
    ] = {}
    for offset, pos in enumerate(positions):
        for other_pos in positions[offset + 1 :]:
            distances[pos, other_pos] = distance(pos, other_pos)

    distances = dict(sorted(distances.items(), key=lambda item: item[1]))

    print("Distances:")
    for pair, dis in distances.items():
        print(f"pair={pair}, distance={dis}")
    print()

    pair = connect(distances, len(positions))

    return pair[0][0] * pair[1][0]


def connect(  # noqa: C901
    distances: dict[tuple[tuple[int, int, int], tuple[int, int, int]], float],
    n_boxes: int,
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Create circuits."""
    connected: dict[tuple[int, int, int], int] = {}
    circuits: dict[int, list[tuple[int, int, int]]] = {}

    from_box = to_box = (0, 0, 0)
    for from_box, to_box in distances:
        from_box_connect = connected.get(from_box)
        to_box_connect = connected.get(to_box)
        if from_box_connect is not None and to_box_connect is not None:
            if from_box_connect != to_box_connect:
                # Merge circuits
                source = circuits[to_box_connect]
                target = circuits[from_box_connect]
                target += source
                circuits[to_box_connect] = []
                for c in source:
                    connected[c] = from_box_connect
                if len(target) >= n_boxes:
                    break
        elif from_box_connect is not None:
            # Append to_box to from_box circuit
            target = circuits[from_box_connect]
            target.append(to_box)
            connected[to_box] = from_box_connect
            if len(target) >= n_boxes:
                break
        elif to_box_connect is not None:
            # Append from_box to to_box circuit
            target = circuits[to_box_connect]
            target.append(from_box)
            connected[from_box] = to_box_connect
            if len(target) >= n_boxes:
                break
        elif from_box_connect is None and to_box_connect is None:
            # Append new circuit
            idx = len(circuits)
            target = [from_box, to_box]
            circuits[idx] = target
            connected[from_box] = idx
            connected[to_box] = idx
            if len(target) >= n_boxes:
                break

    return from_box, to_box


def distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    """Compute distance in 3D space."""
    return math.sqrt(sum((a_ - b_) ** 2 for a_, b_ in zip(a, b, strict=True)))


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
