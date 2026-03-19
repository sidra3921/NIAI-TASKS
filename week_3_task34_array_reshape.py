# Week 3 - Task 34: NumPy Array Reshape
# https://www.w3schools.com/python/numpy_array_reshape.asp

import numpy as np

def main():
    arr = np.arange(1, 13)  # 1..12
    print("Original:", arr, "shape:", arr.shape)

    r1 = arr.reshape(3, 4)
    print("\nReshape to (3,4):\n", r1)

    r2 = arr.reshape(2, 2, 3)
    print("\nReshape to (2,2,3):\n", r2)

    # Use -1 to infer dimension
    r3 = arr.reshape(3, -1)
    print("\nReshape to (3,-1):\n", r3, "shape:", r3.shape)

if __name__ == "__main__":
    main()
