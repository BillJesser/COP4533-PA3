import unittest
from pathlib import Path

from src.weighted_lcs import solve_text, weighted_lcs


ROOT = Path(__file__).resolve().parents[1]


class WeightedLCSTest(unittest.TestCase):
    def test_example_files_match(self) -> None:
        problem_text = (ROOT / "data" / "example.in").read_text(encoding="utf-8")
        expected_output = (ROOT / "data" / "example.out").read_text(encoding="utf-8")
        self.assertEqual(solve_text(problem_text), expected_output)

    def test_weighted_choice_beats_longer_choice(self) -> None:
        values = {"a": 2, "b": 4, "c": 5}
        total_value, subsequence = weighted_lcs(values, "aacb", "caab")
        self.assertEqual(total_value, 9)
        self.assertEqual(subsequence, "cb")


if __name__ == "__main__":
    unittest.main()
