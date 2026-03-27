import sys
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


def solve() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return

    idx = 0
    k = int(data[idx].strip())
    idx += 1

    values: dict[str, int] = {}
    for _ in range(k):
        ch, value = data[idx].split()
        values[ch] = int(value)
        idx += 1

    a = data[idx].rstrip("\n")
    idx += 1
    b = data[idx].rstrip("\n")

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

    def build(i: int, j: int) -> str:
        if i == n or j == m:
            return ""

        if a[i] == b[j]:
            take = values.get(a[i], 0) + best(i + 1, j + 1)
            if best(i, j) == take:
                return a[i] + build(i + 1, j + 1)

        if best(i, j) == best(i + 1, j):
            return build(i + 1, j)
        return build(i, j + 1)

    print(best(0, 0))
    print(build(0, 0))


if __name__ == "__main__":
    solve()
