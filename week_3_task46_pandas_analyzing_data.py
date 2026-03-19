# Week 3 - Task 46: Pandas Data Analyzing
# https://www.w3schools.com/python/pandas_analyzing.asp

import pandas as pd

def main():
    data = {
        "Name": ["Ali", "Sara", "John", "Ayesha", "Bilal"],
        "Age": [20, 22, 19, 21, 20],
        "Score": [88, 92, 75, 85, 90],
    }

    df = pd.DataFrame(data)

    print("DataFrame:")
    print(df)

    print("\nShape (rows, cols):", df.shape)
    print("\nColumns:", df.columns.tolist())

    print("\nInfo:")
    print(df.info())

    print("\nDescribe:")
    print(df.describe())

    print("\nValue counts for Age:")
    print(df["Age"].value_counts())

    print("\nTop 3 by Score:")
    print(df.sort_values(by="Score", ascending=False).head(3))

if __name__ == "__main__":
    main()
