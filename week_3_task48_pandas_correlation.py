# Week 3 - Task 48: Pandas Data Correlation
# https://www.w3schools.com/python/pandas_correlations.asp

import pandas as pd

def main():
    # A small numeric dataset to show correlations
    data = {
        "Hours_Studied": [1, 2, 3, 4, 5, 6],
        "Sleep_Hours": [8, 7, 7, 6, 6, 5],
        "Score": [40, 50, 55, 65, 70, 80],
    }

    df = pd.DataFrame(data)

    print("DataFrame:")
    print(df)

    print("\nCorrelation matrix:")
    corr = df.corr(numeric_only=True)
    print(corr)

    # Example: correlation between Hours_Studied and Score
    print("\nCorrelation (Hours_Studied vs Score):", corr.loc["Hours_Studied", "Score"])

if __name__ == "__main__":
    main()
