# Week 3 - Task 35: NumPy Array Iterating
# https://www.w3schools.com/python/numpy_array_iterating.asp

import numpy as np

def main():
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("Array:\n", arr2)

    print("\nIterate rows:")
    for row in arr2:
        print(row)

    print("\nIterate elements:")
    for x in arr2:
        for y in x:
            print(y, end=" ")
    print()

    print("\nUsing nditer (flat iteration):")
    for v in np.nditer(arr2):
        print(int(v), end=" ")
    print()

if __name__ == "__main__":
    main()
