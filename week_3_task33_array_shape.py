# Week 3 - Task 33: NumPy Array Shape
# https://www.w3schools.com/python/numpy_array_shape.asp

import numpy as np

def main():
    arr1 = np.array([1, 2, 3, 4])
    print("arr1:", arr1, "shape:", arr1.shape)

    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("arr2:\n", arr2, "\nshape:", arr2.shape)

    arr3 = np.array([[[1], [2]], [[3], [4]]])
    print("arr3:\n", arr3, "\nshape:", arr3.shape)

if __name__ == "__main__":
    main()
