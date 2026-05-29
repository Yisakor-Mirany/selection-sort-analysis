import time
import random
from selection_sort import selection_sort


def run_test(description, arr, expected):
    result = selection_sort(arr[:])
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {description}")
    if result != expected:
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")
    return status == "PASS"


def run_all_tests():
    print("=" * 55)
    print("Selection Sort — Test Suite")
    print("=" * 55)

    tests = [
        ("Random array",              [64, 25, 12, 22, 11],         [11, 12, 22, 25, 64]),
        ("Already sorted",            [1, 2, 3, 4, 5],              [1, 2, 3, 4, 5]),
        ("Reverse sorted",            [5, 4, 3, 2, 1],              [1, 2, 3, 4, 5]),
        ("Duplicate values",          [3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
        ("All identical",             [7, 7, 7, 7],                 [7, 7, 7, 7]),
        ("Single element",            [42],                         [42]),
        ("Empty array",               [],                           []),
        ("Two elements sorted",       [1, 2],                       [1, 2]),
        ("Two elements unsorted",     [2, 1],                       [1, 2]),
        ("Negative numbers",          [-3, -1, -4, -1, -5],        [-5, -4, -3, -1, -1]),
        ("Mixed positive/negative",   [3, -2, 0, -5, 8],           [-5, -2, 0, 3, 8]),
        ("Large values",              [10**6, 10**3, 10**9],        [10**3, 10**6, 10**9]),
    ]

    passed = sum(run_test(*t) for t in tests)
    total = len(tests)

    print()
    print(f"Results: {passed}/{total} tests passed")
    print()

    # Descending order test
    print("--- Descending order (optional enhancement) ---")
    arr = [3, 1, 4, 1, 5, 9]
    result = selection_sort(arr[:], descending=True)
    expected = [9, 5, 4, 3, 1, 1]
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] Descending sort: {result}")
    print()


def performance_analysis():
    print("=" * 55)
    print("Performance Analysis")
    print("=" * 55)

    sizes = [100, 500, 1000, 2000, 5000]

    for n in sizes:
        # worst case: reverse sorted
        arr = list(range(n, 0, -1))
        start = time.perf_counter()
        selection_sort(arr)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:8.3f} ms  (reverse-sorted / worst case)")

    print()

    for n in sizes:
        # best case for comparisons: already sorted (still O(n²) comparisons)
        arr = list(range(n))
        start = time.perf_counter()
        selection_sort(arr)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  n={n:>5}: {elapsed:8.3f} ms  (already-sorted)")

    print()


def stability_demonstration():
    print("=" * 55)
    print("Stability Demonstration")
    print("=" * 55)
    print("Selection Sort is NOT stable.")
    print()
    print("Example: sort [(3,a), (3,b), (1,c)] by first element.")
    print("  - (3,a) and (3,b) are equal; original order a < b.")
    print("  - Selection Sort may swap (3,a) with (1,c), placing")
    print("    (3,b) before (3,a) — original order not preserved.")
    print()
    # Simulate with tagged pairs
    data = [(3, 'a'), (3, 'b'), (1, 'c')]
    n = len(data)
    arr = data[:]
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f"  Input:  {data}")
    print(f"  Output: {arr}")
    equal_keys = [(v, tag) for v, tag in arr if v == 3]
    if equal_keys[0][1] != 'a':
        print("  => Original order of equal elements NOT preserved (unstable).")
    else:
        print("  => Original order preserved for this input (but not guaranteed).")
    print()


if __name__ == "__main__":
    run_all_tests()
    performance_analysis()
    stability_demonstration()
