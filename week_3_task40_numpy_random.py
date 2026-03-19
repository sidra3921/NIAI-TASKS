# Week 3 - Task 40: NumPy Random
# https://www.w3schools.com/python/numpy_random.asp

import numpy as np

def main():
    np.random.seed(42)  # reproducible results

    print("randint(0, 100):", np.random.randint(0, 100))
    print("randint(0, 100, size=5):", np.random.randint(0, 100, size=5))

    print("\nrand() single:", np.random.rand())
    print("rand(2,3):\n", np.random.rand(2, 3))

    print("\nchoice from [1,2,3,4]:", np.random.choice([1, 2, 3, 4], size=6))

    # Normal distribution
    normal = np.random.normal(loc=0.0, scale=1.0, size=5)
    print("\nnormal(loc=0, scale=1, size=5):", normal)

if __name__ == "__main__":
    main()
