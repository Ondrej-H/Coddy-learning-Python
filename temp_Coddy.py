
contact_book = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    "Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}
}


if not contact_book:
        print("No contacts available.")
else:
    for name, list_of_contacts in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {list_of_contacts["phone"]}")
        print(f"Email: {list_of_contacts["email"]}")
        print(f"Address: {list_of_contacts["address"]}\n")
        #for contact_type, contact_data in list_of_contacts:
