"""
Week 2 - Task 50: Standard Deviation and Variance

This script demonstrates:
1) What standard deviation and variance mean (conceptually)
2) How to calculate variance and standard deviation manually (so you understand it)
3) How to calculate them using NumPy: numpy.var() and numpy.std()
"""

import math
from typing import List, Tuple


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute mean of an empty list.")
    return sum(values) / len(values)


def variance_population(values: List[float]) -> float:
    """
    Population variance (divide by N), same idea as W3Schools example.
    """
    if not values:
        raise ValueError("Cannot compute variance of an empty list.")
    m = mean(values)
    squared_diffs = [(x - m) ** 2 for x in values]
    return sum(squared_diffs) / len(values)


def std_population(values: List[float]) -> float:
    """Population standard deviation = sqrt(population variance)."""
    return math.sqrt(variance_population(values))


def numpy_demo(values: List[float]) -> None:
    print("\n--- NumPy calculations (if installed) ---")
    try:
        import numpy as np
    except ImportError:
        print("NumPy is not installed. Skipping numpy.var() and numpy.std().")
        return

    print("NumPy variance (var):", float(np.var(values)))
    print("NumPy std (std)     :", float(np.std(values)))


def print_results(label: str, values: List[float]) -> None:
    print(f"\n{label}")
    print("Data:", values)

    m = mean(values)
    var = variance_population(values)
    std = math.sqrt(var)

    print("Mean (average):", round(m, 2))
    print("Variance      :", round(var, 2))
    print("Std deviation :", round(std, 2))

    numpy_demo(values)


def main():
    # Example 1 (low spread)
    speed1 = [86, 87, 88, 86, 87, 85, 86]
    print_results("--- Example 1 (low spread) ---", speed1)

    # Example 2 (wide spread)
    speed2 = [32, 111, 138, 28, 59, 77, 97]
    print_results("--- Example 2 (wide spread) ---", speed2)


if __name__ == "__main__":
    main()
