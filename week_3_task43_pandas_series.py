# Week 3 - Task 43: Pandas Series
# https://www.w3schools.com/python/pandas_series.asp

import pandas as pd

def main():
    a = [10, 20, 30]
    s1 = pd.Series(a)
    print("Series from list:")
    print(s1)

    s2 = pd.Series(a, index=["x", "y", "z"])
    print("\nSeries with custom index:")
    print(s2)
    print("Value at index 'y':", s2["y"])

    # Series from dictionary
    calories = {"day1": 420, "day2": 380, "day3": 390}
    s3 = pd.Series(calories)
    print("\nSeries from dict:")
    print(s3)

    # Select subset
    s4 = pd.Series(calories, index=["day1", "day3"])
    print("\nSubset with index filter:")
    print(s4)

if __name__ == "__main__":
    main()
