"""
Week 2 - Task 26: Python Exception Handling (try/except/else/finally)

This script demonstrates:
1) Handling ZeroDivisionError
2) Handling IndexError
3) Using try/except/else
4) Using try/except/finally
"""


def divide_numbers(numerator: float, denominator: float) -> float:
    """Divide two numbers with ZeroDivisionError handling."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")
        return float("nan")


def access_list_item(items, index: int):
    """Access a list item with IndexError handling."""
    try:
        return items[index]
    except IndexError:
        print("Index Out of Bound.")
        return None


def reciprocal_of_even():
    """
    Ask user for a number.
    - If not even, print message (AssertionError handled)
    - If even, compute reciprocal in else block
    Note: If user enters 0, ZeroDivisionError will occur (same behavior as tutorial example).
    """
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except (ValueError, AssertionError):
        print("Not an even number!")
    else:
        reciprocal = 1 / num
        print("Reciprocal:", reciprocal)


def finally_demo():
    """Demonstrate finally block always runs."""
    try:
        numerator = 10
        denominator = 0
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")
    finally:
        print("This is finally block.")


def main():
    print("1) ZeroDivisionError example:")
    print("Result:", divide_numbers(10, 0))
    print()

    print("2) IndexError example:")
    even_numbers = [2, 4, 6, 8]
    print("Item:", access_list_item(even_numbers, 5))
    print()

    print("3) try/except/else example:")
    reciprocal_of_even()
    print()

    print("4) try/except/finally example:")
    finally_demo()


if __name__ == "__main__":
    main()
