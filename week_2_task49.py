"""
Week 2 - Task 49: Mean, Median, Mode

This script demonstrates:
1) How to calculate mean/median/mode manually (logic first)
2) How to calculate mean/median using NumPy
3) How to calculate mode using SciPy (stats.mode)
"""

from collections import Counter
from typing import List, Tuple


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute mean of an empty list.")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute median of an empty list.")

    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return float(sorted_values[mid])

    # even length: average the two middle values
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def mode(values: List[float]) -> Tuple[List[float], int]:
    """
    Returns (modes, frequency).
    If multiple values share the same highest frequency, returns all of them.
    """
    if not values:
        raise ValueError("Cannot compute mode of an empty list.")

    counts = Counter(values)
    max_freq = max(counts.values())
    modes = [val for val, freq in counts.items() if freq == max_freq]
    return sorted(modes), max_freq


def numpy_and_scipy_demo(values: List[float]) -> None:
    print("\n--- Using NumPy / SciPy (if installed) ---")

    try:
        import numpy as np
    except ImportError:
        print("NumPy is not installed. Skipping NumPy mean/median.")
        np = None

    try:
        from scipy import stats
    except ImportError:
        print("SciPy is not installed. Skipping SciPy mode.")
        stats = None

    if np is not None:
        print("NumPy mean  :", float(np.mean(values)))
        print("NumPy median:", float(np.median(values)))

    if stats is not None:
        # SciPy's mode API has changed over versions; keep it simple:
        result = stats.mode(values, keepdims=True)
        # result.mode and result.count are arrays
        print("SciPy mode  :", result.mode[0])
        print("Mode count  :", int(result.count[0]))


def main():
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    print("Data:", speed)

    # Manual (logic-based) calculations
    print("\n--- Manual calculations (no libraries) ---")
    print("Mean  :", round(mean(speed), 2))
    print("Median:", median(speed))
    modes, freq = mode(speed)
    print("Mode(s):", modes, "| frequency:", freq)

    # Library-based calculations (as in tutorial)
    numpy_and_scipy_demo(speed)


if __name__ == "__main__":
    main()
