from collections import OrderedDict


def lru_cache(maxsize=None):
    def decorator(func):
        cache = OrderedDict()

        def wrapper(i: int, j: int) -> int:
            key = (i, j)
            if key in cache:
                cache.move_to_end(key)
                return cache[key]

            result = func(i, j)
            cache[key] = result

            if maxsize is not None and len(cache) > maxsize:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator


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

    @lru_cache(maxsize=None)
    def best(i: int, j: int) -> int:
        if i == n or j == m:
            return 0

        answer = max(best(i + 1, j), best(i, j + 1))
        if a[i] == b[j]:
            answer = max(answer, values.get(a[i], 0) + best(i + 1, j + 1))
        return answer

    i = 0
    j = 0
    subsequence: list[str] = []

    while i < n and j < m:
        current = best(i, j)

        if a[i] == b[j]:
            take = values.get(a[i], 0) + best(i + 1, j + 1)
            if current == take:
                subsequence.append(a[i])
                i += 1
                j += 1
                continue

        if current == best(i + 1, j):
            i += 1
        else:
            j += 1

    return best(0, 0), "".join(subsequence)


def solve_text(text: str) -> str:
    values, a, b = parse_input(text)
    total_value, subsequence = weighted_lcs(values, a, b)
    return f"{total_value}\n{subsequence}\n"
