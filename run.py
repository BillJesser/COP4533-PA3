import argparse
import sys
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

    answer = solve_text(problem_text)

    if args.output:
        Path(args.output).write_text(answer, encoding="utf-8")
    else:
        sys.stdout.write(answer)


if __name__ == "__main__":
    main()
