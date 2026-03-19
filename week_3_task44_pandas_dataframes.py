# Week 3 - Task 44: Pandas DataFrames
# https://www.w3schools.com/python/pandas_dataframes.asp

import pandas as pd

def main():
    data = {
        "Calories": [420, 380, 390],
        "Duration": [50, 40, 45],
    }

    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

    print("\nRow 0 using loc:")
    print(df.loc[0])

    print("\nRows 0 and 1 using loc:")
    print(df.loc[[0, 1]])

    # Custom index
    df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print("\nDataFrame with custom index:")
    print(df2)

    print("\nRow 'day2':")
    print(df2.loc["day2"])

if __name__ == "__main__":
    main()
