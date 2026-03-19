# Week 3 - Task 30: NumPy Array Slicing
# https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np

def main():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("arr:", arr)
    print("arr[2:6]:", arr[2:6])
    print("arr[:5]:", arr[:5])
    print("arr[5:]:", arr[5:])
    print("arr[-5:-2]:", arr[-5:-2])
    print("arr[::2] (step=2):", arr[::2])
    print("arr[1::2] (odd indices):", arr[1::2])

    arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    print("\narr2:\n", arr2)
    print("arr2[0:2, 1:3]:\n", arr2[0:2, 1:3])  # first 2 rows, last 2 cols

if __name__ == "__main__":
    main()
