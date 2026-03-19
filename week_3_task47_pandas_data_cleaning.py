# Week 3 - Task 47: Pandas Data Cleaning Techniques
# https://www.w3schools.com/python/pandas_cleaning.asp

import pandas as pd

def main():
    # Example dataset with:
    # - missing values (None)
    # - duplicates
    # - wrong format (Age as string)
    data = {
        "Name": ["Ali", "Sara", "Sara", "John", None],
        "Age": ["20", "22", "22", "N/A", "21"],
        "City": ["Lahore", "Karachi", "Karachi", "NYC", "Islamabad"],
    }

    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    # 1) Drop missing values
    df_no_na = df.dropna()
    print("\nAfter dropna():")
    print(df_no_na)

    # 2) Remove duplicates
    df_no_dupes = df_no_na.drop_duplicates()
    print("\nAfter drop_duplicates():")
    print(df_no_dupes)

    # 3) Convert Age to numeric (coerce invalid to NaN), then drop invalid rows
    df_no_dupes["Age"] = pd.to_numeric(df_no_dupes["Age"], errors="coerce")
    df_clean = df_no_dupes.dropna(subset=["Age"])
    df_clean["Age"] = df_clean["Age"].astype(int)

    print("\nAfter cleaning Age column (numeric only):")
    print(df_clean)

if __name__ == "__main__":
    main()
