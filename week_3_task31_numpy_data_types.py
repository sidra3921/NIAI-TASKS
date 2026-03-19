# Week 3 - Task 31: NumPy Data Types
# https://www.w3schools.com/python/numpy_data_types.asp

import numpy as np

def main():
    arr_int = np.array([1, 2, 3, 4])
    print("arr_int dtype:", arr_int.dtype)

    arr_str = np.array(["a", "b", "c"])
    print("arr_str dtype:", arr_str.dtype)

    # Creating with explicit dtype
    arr_float32 = np.array([1, 2, 3], dtype=np.float32)
    print("arr_float32:", arr_float32, "dtype:", arr_float32.dtype)

    # Type conversion (astype)
    arr_as_int = arr_float32.astype(np.int32)
    print("Converted to int32:", arr_as_int, "dtype:", arr_as_int.dtype)

    # Check itemsize
    print("int32 itemsize:", np.dtype(np.int32).itemsize, "bytes")

if __name__ == "__main__":
    main()
