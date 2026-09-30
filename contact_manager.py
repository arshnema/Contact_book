def create_contact(contacts):
    name = input("Enter your name = ")
    if name in contacts:
        print(f"Contact name {name} already exists!")
        return
    age = input("Enter age = ")
    email = input("Enter email = ")
    mobile = input("Enter mobile number = ")
    contacts[name] = {
        "age": int(age),
        "email": email,
        "mobile": mobile
    } 
    print(f"Contact name {name} has been created successfully!")
def view_contact(contacts):
    name = input("Enter contact name to view = ")
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Age: {contact['age']}")
        print(f"Email: {contact['email']}")
        print(f"Mobile number: {contact['mobile']}")
    else:
        print("Contact not found!")
def update_contact(contacts):
    name = input("Enter name to update contact = ")
    if name in contacts:
        age = input("Enter updated age = ")
        email = input("Enter updated email = ")
        mobile = input("Enter updated mobile number = ")
        contacts[name] = {
            "age": int(age),
            "email": email,
            "mobile": mobile
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
def delete_contact(contacts):
    name = input("Enter contact name to delete = ")
    if name in contacts:
        del contacts[name]
        print(f"Contact name {name} has been deleted successfully!")
    else:
        print("Contact not found!")
def count_contacts(contacts):
    print(f"Total contacts in your book: {len(contacts)}")
