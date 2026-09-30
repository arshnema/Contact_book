def search_contact(contacts):
    search_name = input("Enter contact name to search = ")

    found = False

    for name, contact in contacts.items():
        if search_name.lower() in name.lower():
            print(
                f"Found - Name: {name}, "
                f"Age: {contact['age']}, "
                f"Mobile number: {contact['mobile']}, "
                f"Email: {contact['email']}"
            )
            found = True

    if not found:
        print("No contact found with that name!")