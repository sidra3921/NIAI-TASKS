# Week 3 - Task 42: Pandas Installation / Getting Started
# https://www.w3schools.com/python/pandas_getting_started.asp

def main():
    """
    This task is mainly about installing and checking Pandas.

    Install (in terminal):
      pip install pandas

    Check version:
      import pandas as pd
      print(pd.__version__)
    """
    try:
        import pandas as pd
        print("Pandas is installed ✅")
        print("Pandas version:", pd.__version__)
    except ImportError:
        print("Pandas is NOT installed ❌")
        print("Install it using: pip install pandas")

if __name__ == "__main__":
    main()
