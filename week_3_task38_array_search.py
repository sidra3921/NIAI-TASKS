# Week 3 - Task 38: NumPy Array Searching
# https://www.w3schools.com/python/numpy_array_search.asp

import numpy as np

def main():
    arr = np.array([5, 7, 7, 8, 9, 7, 10])

    print("arr:", arr)

    idx = np.where(arr == 7)
    print("Indices where value == 7:", idx)

    # Search condition
    idx2 = np.where(arr % 2 == 0)
    print("Indices of even numbers:", idx2)

    # searchsorted works on sorted arrays
    sorted_arr = np.array([1, 3, 5, 7, 9])
    pos = np.searchsorted(sorted_arr, 6)
    print("\nsorted_arr:", sorted_arr)
    print("Position to insert 6 to keep sorted:", pos)

if __name__ == "__main__":
    main()
