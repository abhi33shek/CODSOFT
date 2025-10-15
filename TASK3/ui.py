def menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def input_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    return name, phone, email, address

def _format_row(cols, widths):
    """Format a row given column values and target widths."""
    parts = []
    for i, text in enumerate(cols):
        s = str(text)
        if len(s) > widths[i]:
            s = s[:widths[i] - 1] + "…" if widths[i] > 1 else s[:widths[i]]
        parts.append(s.ljust(widths[i]))
    return "| " + " | ".join(parts) + " |"

def _print_separator(widths):
    line = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    print(line)

def print_contacts_table(contacts):
    """Print a numbered table of contacts without external libs."""
    if not contacts:
        print("No contacts to display.")
        return

    headers = ["No.", "Name", "Phone", "Email", "Address"]
    rows = []
    for i, c in enumerate(contacts, start=1):
        rows.append([i, c.name, c.phone, c.email, c.address])

    # Compute column widths
    col_count = len(headers)
    widths = [0] * col_count
    # Header widths
    for i, h in enumerate(headers):
        widths[i] = max(widths[i], len(str(h)))
    # Row widths
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))

    # Print table
    _print_separator(widths)
    print(_format_row(headers, widths))
    _print_separator(widths)
    for row in rows:
        print(_format_row(row, widths))
    _print_separator(widths)

def select_contact(results):
    """
    Let the user choose a contact from a results list.
    Returns the zero-based index within the 'results' list, or None.
    """
    if not results:
        print("No contacts found.")
        return None

    print_contacts_table(results)

    while True:
        raw = input("Select contact (No.) or press Enter to cancel: ").strip()
        if raw == "":
            return None
        try:
            choice = int(raw)
            idx = choice - 1
            if 0 <= idx < len(results):
                return idx
            else:
                print(f"Please enter a number between 1 and {len(results)}.")
        except ValueError:
            print("Please enter a valid number.")
