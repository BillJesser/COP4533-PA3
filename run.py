import argparse
import sys
import time
from pathlib import Path

from src.weighted_lcs import solve_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute a maximum-value common subsequence for two strings."
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Optional input file path. If omitted, input is read from standard input.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output file path. If omitted, output is written to standard output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.input:
        problem_text = Path(args.input).read_text(encoding="utf-8")
    else:
        problem_text = sys.stdin.read()

    start = time.perf_counter()
    answer = solve_text(problem_text)
    elapsed_ms = (time.perf_counter() - start) * 1000.0

    if args.output:
        Path(args.output).write_text(answer, encoding="utf-8")
    else:
        sys.stdout.write(answer)

    sys.stderr.write(f"Execution time: {elapsed_ms:.3f} ms\n")


if __name__ == "__main__":
    main()
