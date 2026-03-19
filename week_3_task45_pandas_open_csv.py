# Week 3 - Task 45: Pandas Open CSV Files
# https://www.w3schools.com/python/pandas_csv.asp

from pathlib import Path
import pandas as pd

def create_sample_csv(path: Path) -> None:
    sample = """Name,Age,City
Ali,20,Lahore
Sara,22,Karachi
John,19,NYC
Ayesha,21,Islamabad
"""
    path.write_text(sample, encoding="utf-8")

def main():
    csv_path = Path("sample_people.csv")

    if not csv_path.exists():
        create_sample_csv(csv_path)
        print(f"Created sample CSV: {csv_path.resolve()}")

    df = pd.read_csv(csv_path)
    print("\nLoaded DataFrame from CSV:")
    print(df)

    print("\nFirst 2 rows:")
    print(df.head(2))

if __name__ == "__main__":
    main()
