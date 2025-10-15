"""
main.py - CLI Calculator (Task 2)
"""

from engine import OPERATORS
from ui import read_number, read_operator, print_result, ask_continue

def main():
    print("=" * 48)
    print(" Calculator - CodSoft Task 2")
    print("=" * 48)

    while True:
        try:
            a = read_number("first")
            b = read_number("second")
            op = read_operator(OPERATORS.keys())

            name, func = OPERATORS[op]
            result = func(a, b)
            print_result(a, op, b, result, name)

            if not ask_continue():
                break

            print("\n" + "-" * 48 + "\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}.")
        except KeyboardInterrupt:
            print("\nInterrupted.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    print("\nThank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    main()
