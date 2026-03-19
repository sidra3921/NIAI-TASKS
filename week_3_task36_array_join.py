# Week 3 - Task 36: NumPy Array Join (concatenate/stack)
# https://www.w3schools.com/python/numpy_array_join.asp

import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("a:", a)
    print("b:", b)

    joined = np.concatenate((a, b))
    print("\nconcatenate:", joined)

    a2 = np.array([[1, 2], [3, 4]])
    b2 = np.array([[5, 6], [7, 8]])

    print("\na2:\n", a2)
    print("b2:\n", b2)

    join_axis0 = np.concatenate((a2, b2), axis=0)
    join_axis1 = np.concatenate((a2, b2), axis=1)

    print("\nconcatenate axis=0:\n", join_axis0)
    print("\nconcatenate axis=1:\n", join_axis1)

    print("\nstack (new axis):\n", np.stack((a, b), axis=0))
    print("hstack:\n", np.hstack((a2, b2)))
    print("vstack:\n", np.vstack((a2, b2)))

if __name__ == "__main__":
    main()
