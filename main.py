from contact_manager import (
    create_contact,
    view_contact,
    update_contact,
    delete_contact,
    count_contacts
)

from search import search_contact


contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input("Enter your choice = ")

    if choice == "1":
        create_contact(contacts)

    elif choice == "2":
        view_contact(contacts)

    elif choice == "3":
        update_contact(contacts)

    elif choice == "4":
        delete_contact(contacts)

    elif choice == "5":
        search_contact(contacts)

    elif choice == "6":
        count_contacts(contacts)

    elif choice == "7":
        print("Goodbye... Closing the program")
        break

    else:
        print("Invalid input")