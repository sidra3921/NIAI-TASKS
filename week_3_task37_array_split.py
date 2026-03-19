# Week 3 - Task 37: NumPy Array Splitting
# https://www.w3schools.com/python/numpy_array_split.asp

import numpy as np

def main():
    arr = np.array([1, 2, 3, 4, 5, 6])
    parts = np.array_split(arr, 3)

    print("arr:", arr)
    print("Split into 3 parts:", parts)

    arr2 = np.arange(1, 13).reshape(3, 4)
    print("\narr2:\n", arr2)

    split_rows = np.array_split(arr2, 3, axis=0)
    split_cols = np.array_split(arr2, 2, axis=1)

    print("\nSplit rows (axis=0):")
    for p in split_rows:
        print(p)

    print("\nSplit cols (axis=1):")
    for p in split_cols:
        print(p)

if __name__ == "__main__":
    main()
