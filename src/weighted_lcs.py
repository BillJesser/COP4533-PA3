def parse_input(text: str) -> tuple[dict[str, int], str, str]:
    lines = text.splitlines()
    if not lines:
        raise ValueError("Input is empty.")

    idx = 0
    k = int(lines[idx].strip())
    idx += 1

    values: dict[str, int] = {}
    for _ in range(k):
        ch, value = lines[idx].split()
        values[ch] = int(value)
        idx += 1

    if idx >= len(lines):
        raise ValueError("Missing first string A.")
    a = lines[idx]
    idx += 1

    if idx >= len(lines):
        raise ValueError("Missing second string B.")
    b = lines[idx]

    return values, a, b


def weighted_lcs(values: dict[str, int], a: str, b: str) -> tuple[int, str]:
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            best = max(dp[i + 1][j], dp[i][j + 1])
            if a[i] == b[j]:
                best = max(best, values.get(a[i], 0) + dp[i + 1][j + 1])
            dp[i][j] = best

    i = 0
    j = 0
    subsequence: list[str] = []

    while i < n and j < m:
        current = dp[i][j]

        if a[i] == b[j]:
            take = values.get(a[i], 0) + dp[i + 1][j + 1]
            if current == take:
                subsequence.append(a[i])
                i += 1
                j += 1
                continue

        if current == dp[i + 1][j]:
            i += 1
        else:
            j += 1

    return dp[0][0], "".join(subsequence)


def solve_text(text: str) -> str:
    values, a, b = parse_input(text)
    total_value, subsequence = weighted_lcs(values, a, b)
    return f"{total_value}\n{subsequence}\n"
