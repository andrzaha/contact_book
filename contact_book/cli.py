# cli.py
import sys
from contact import Contact
from utils import print_contacts

def main():
    contact_book = Contact()

    if len(sys.argv) < 2:
        print("Usage: python cli.py [add|remove|get] [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 5:
            print("Usage: python cli.py add [name] [phone] [email]")
            return
        name, phone, email = sys.argv[2], sys.argv[3], sys.argv[4]
        contact_book.add_contact(name, phone, email)
        print("Contact added successfully!")

    elif command == "remove":
        if len(sys.argv) != 3:
            print("Usage: python cli.py remove [contact_id]")
            return
        contact_id = int(sys.argv[2])
        contact_book.remove_contact(contact_id)
        print("Contact removed successfully!")

    elif command == "get":
        contacts = contact_book.get_contacts()
        print_contacts(contacts)

    else:
        print("Unknown command. Use add, remove, or get.")

if __name__ == "__main__":
    main()
