# Week 3 - Task 41: Pandas Basics
# https://www.w3schools.com/python/pandas_tutorial.asp

import pandas as pd

def main():
    data = {
        "Name": ["Ali", "Sara", "John", "Ayesha"],
        "Age": [20, 22, 19, 21],
        "City": ["Lahore", "Karachi", "NYC", "Islamabad"],
    }

    df = pd.DataFrame(data)

    print("DataFrame:")
    print(df)

    print("\nFirst 2 rows (head):")
    print(df.head(2))

    print("\nBasic info:")
    print(df.info())

    print("\nDescribe numeric columns:")
    print(df.describe())

if __name__ == "__main__":
    main()
