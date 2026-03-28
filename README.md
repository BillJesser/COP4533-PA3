# COP4533-PA3

## Students

- William Jesser, UFID 5963-4986

## Project Layout

```text
COP4533-PA3/
|-- data/
|   |-- example.in
|   `-- example.out
|-- src/
|   |-- __init__.py
|   `-- weighted_lcs.py
|-- tests/
|   `-- test_weighted_lcs.py
|-- .gitignore
|-- README.md
`-- run.py
```

## Overview

This project solves the weighted common subsequence problem in Python. Given two strings and a
nonnegative value for each character, the program prints:

1. The maximum total value of a common subsequence
2. One optimal subsequence that achieves that value

The solver uses top-down dynamic programming with memoization and reconstructs one optimal
answer from the cached results.

## Requirements

- Python 3.9 or newer
- No third-party dependencies

## Build / Compile

No build step is required.

Optional syntax check:

```powershell
python -m py_compile .\run.py .\src\weighted_lcs.py
```

## Running The Program

The easiest way to run the program is to pass an input file path directly:

```powershell
python .\run.py .\data\example.in
```

You can also write the result to a file:

```powershell
python .\run.py .\data\example.in --output .\data\result.out
```

If you prefer standard input, that still works:

```powershell
Get-Content .\data\example.in | python .\run.py
```

## Example Input And Output

- Example input: `data/example.in`
- Expected output: `data/example.out`

To reproduce the provided example output:

```powershell
python .\run.py .\data\example.in
```

The program output should match `data/example.out`.

## Running Tests

```powershell
python -m unittest discover -s .\tests -v
```

## Assumptions

- Input format is:
  - Line 1: `K`, the number of characters with assigned values
  - Next `K` lines: a character and its nonnegative integer value
  - Next line: string `A`
  - Next line: string `B`
- If multiple optimal subsequences exist, any one of them is acceptable
- Characters not listed in the value table are treated as value `0`
