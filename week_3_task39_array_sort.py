# Week 3 - Task 39: NumPy Array Sorting
# https://www.w3schools.com/python/numpy_array_sort.asp

import numpy as np

def main():
    arr = np.array([3, 2, 0, 1])
    print("Original:", arr)
    print("Sorted  :", np.sort(arr))

    arr2 = np.array([[3, 2, 4], [5, 0, 1]])
    print("\nOriginal 2D:\n", arr2)
    print("Sorted 2D:\n", np.sort(arr2))  # sorts each row

    arr_str = np.array(["banana", "cherry", "apple"])
    print("\nStrings:", arr_str)
    print("Sorted :", np.sort(arr_str))

if __name__ == "__main__":
    main()
