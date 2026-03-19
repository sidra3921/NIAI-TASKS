# Week 3 - Task 28: NumPy Creating Arrays
# https://www.w3schools.com/python/numpy_creating_arrays.asp

import numpy as np

def main():
    a0 = np.array([1, 2, 3, 4])
    a1 = np.array([[1, 2], [3, 4]])
    a2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    print("1D array:", a0)
    print("2D array:\n", a1)
    print("3D array:\n", a2)

    # Common constructors
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    arange = np.arange(0, 10, 2)

    print("\nzeros:\n", zeros)
    print("ones:\n", ones)
    print("arange(0,10,2):", arange)

if __name__ == "__main__":
    main()
