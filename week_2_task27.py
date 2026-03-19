"""
Week 2 - Task 27: Python Custom Exceptions

What this script shows (with understanding):
- How to define a custom exception by inheriting from Exception
- How to raise it when business rules are violated
- How to catch it using try/except
- How to store extra info (like the invalid value) inside the exception
"""


class AgeTooLowError(Exception):
    """Raised when the user's age is below the required minimum."""

    def __init__(self, age: int, min_age: int = 18, message: str | None = None):
        self.age = age
        self.min_age = min_age
        if message is None:
            message = f"Invalid age: {age}. Minimum allowed is {min_age}."
        super().__init__(message)


def check_voting_eligibility(age: int, min_age: int = 18) -> bool:
    """
    Business rule:
    - If age < min_age => raise AgeTooLowError
    - Else => eligible
    """
    if age < min_age:
        raise AgeTooLowError(age=age, min_age=min_age)
    return True


def main():
    try:
        user_input = input("Enter your age: ").strip()
        age = int(user_input)

        # We call a function that may raise our custom exception
        if check_voting_eligibility(age):
            print("Eligible to vote ✅")

    except ValueError:
        # Happens when int(user_input) fails (e.g., 'abc')
        print("Please enter a valid number for age.")

    except AgeTooLowError as e:
        # Our custom exception is caught here
        print("Exception occurred:", e)
        # Show that the exception stores useful info
        print(f"(Debug info) age={e.age}, min_age={e.min_age}")


if __name__ == "__main__":
    main()
