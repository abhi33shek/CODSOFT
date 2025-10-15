"""
ui.py - Input/output and validation
"""

def read_number(label):
    while True:
        s = input(f"Enter {label} number: ").strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid number. Try again.")

def read_operator(allowed):
    print("\nOperations: +  -  *  /  //  %  **")
    while True:
        op = input("Choose operation: ").strip()
        if op in allowed:
            return op
        print("Invalid operator. Choose from + - * / // % **")

def print_result(a, op, b, result, name):
    # Format integers without .0 for readability
    def fmt(x):
        return int(x) if isinstance(x, float) and x.is_integer() else x
    print(f"\n{name}: {fmt(a)} {op} {fmt(b)} = {fmt(result)}")

def ask_continue():
    ans = input("\n Wanna Another Round? (y/N): ").strip().lower()
    return ans in ('y', 'yes')
