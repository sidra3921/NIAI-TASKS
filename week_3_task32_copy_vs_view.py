# Week 3 - Task 32: NumPy Copy vs View
# https://www.w3schools.com/python/numpy_copy_vs_view.asp

import numpy as np

def main():
    arr = np.array([1, 2, 3, 4, 5])

    view_arr = arr.view()
    copy_arr = arr.copy()

    print("Original:", arr)
    print("View    :", view_arr)
    print("Copy    :", copy_arr)

    # Modify original -> view changes, copy does not
    arr[0] = 999
    print("\nAfter arr[0] = 999")
    print("Original:", arr)
    print("View    :", view_arr)
    print("Copy    :", copy_arr)

    print("\nBase of view (points to original):", view_arr.base is not None)
    print("Base of copy (independent):", copy_arr.base is None)

if __name__ == "__main__":
    main()
