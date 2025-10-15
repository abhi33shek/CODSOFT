from book import ContactBook
from ui import menu, input_contact, select_contact, print_contacts_table

def main():
    book = ContactBook()
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            name, phone, email, address = input_contact()
            book.add_contact(name, phone, email, address)
            print("Contact added.")
        elif choice == "2":
            print_contacts_table(book.list_contacts())
        elif choice == "3":
            q = input("Enter name or phone to search: ").strip()
            results = book.search(q)
            print_contacts_table(results)
        elif choice == "4":
            q = input("Enter name or phone to search: ").strip()
            results = book.search(q)
            idx = select_contact(results)
            if idx is not None:
                c = results[idx]
                print("Leave empty to keep original value.")
                name = input(f"New name [{c.name}]: ") or c.name
                phone = input(f"New phone [{c.phone}]: ") or c.phone
                email = input(f"New email [{c.email}]: ") or c.email
                address = input(f"New address [{c.address}]: ") or c.address
                # Map back to master list index
                try:
                    master_idx = book.contacts.index(c)
                    book.update_contact(master_idx, name=name, phone=phone, email=email, address=address)
                    print("Contact updated.")
                except ValueError:
                    print("Selected contact no longer exists.")
        elif choice == "5":
            q = input("Enter name or phone to search: ").strip()
            results = book.search(q)
            idx = select_contact(results)
            if idx is not None:
                c = results[idx]
                try:
                    master_idx = book.contacts.index(c)
                    book.delete_contact(master_idx)
                    print("Contact deleted.")
                except ValueError:
                    print("Selected contact no longer exists.")
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
