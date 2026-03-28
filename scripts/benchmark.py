import csv
import random
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.weighted_lcs import solve_text


BENCH_DIR = ROOT / "data" / "benchmarks"
RESULTS_PATH = BENCH_DIR / "runtime_results.csv"
ALPHABET = [("a", 2), ("b", 4), ("c", 5), ("d", 3), ("e", 7), ("f", 1)]
LENGTHS = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
REPEATS = 15


def mutate(base: str, rng: random.Random, mutation_rate: float = 0.30) -> str:
    chars = [ch for ch, _ in ALPHABET]
    result: list[str] = []
    for ch in base:
        if rng.random() < mutation_rate:
            result.append(rng.choice(chars))
        else:
            result.append(ch)
    return "".join(result)


def write_problem(path: Path, a: str, b: str) -> None:
    lines = [str(len(ALPHABET))]
    lines.extend(f"{ch} {value}" for ch, value in ALPHABET)
    lines.append(a)
    lines.append(b)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_inputs() -> list[Path]:
    BENCH_DIR.mkdir(parents=True, exist_ok=True)
    created_paths: list[Path] = []

    for index, length in enumerate(LENGTHS, start=1):
        rng = random.Random(4533 + index)
        chars = [ch for ch, _ in ALPHABET]
        base = "".join(rng.choice(chars) for _ in range(length))
        a = mutate(base, rng)
        b = mutate(base, rng)

        path = BENCH_DIR / f"bench_{index:02d}.in"
        write_problem(path, a, b)
        created_paths.append(path)

    return created_paths


def benchmark(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for path in paths:
        problem_text = path.read_text(encoding="utf-8")
        lengths = problem_text.splitlines()
        a = lengths[-2]
        b = lengths[-1]

        samples_ms: list[float] = []
        for _ in range(REPEATS):
            start = time.perf_counter()
            solve_text(problem_text)
            elapsed_ms = (time.perf_counter() - start) * 1000.0
            samples_ms.append(elapsed_ms)

        rows.append(
            {
                "file": path.name,
                "len_a": str(len(a)),
                "len_b": str(len(b)),
                "median_ms": f"{statistics.median(samples_ms):.3f}",
            }
        )

    return rows


def write_results(rows: list[dict[str, str]]) -> None:
    with RESULTS_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["file", "len_a", "len_b", "median_ms"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    paths = generate_inputs()
    rows = benchmark(paths)
    write_results(rows)

    print("file,len_a,len_b,median_ms")
    for row in rows:
        print(f"{row['file']},{row['len_a']},{row['len_b']},{row['median_ms']}")


if __name__ == "__main__":
    main()
