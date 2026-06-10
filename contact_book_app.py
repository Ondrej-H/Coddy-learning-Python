# Contact Book Application

"""
In this project, we will build a Contact Book application step by step by breaking it
into small, manageable functions. The first step is to create a display_menu function.

Create a function named display_menu that prints
the main menu options for the Contact Book.

The menu should include the following options:
Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
"""

def display_menu():
    print("""
Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
""")
    

"""
Now, create the add_contact function that takes one argument: contact_book (a dictionary).
The function should:

1) Get input for the contact's name, phone, email, and address.
2) Check if the name already exists in the dictionary. If it does, print: 
"Contact already exists!".
3) If not, save the contact in the following format:

contact_book[name] = {
	"phone": phone,
	"email": email,
	"address": address
}
Then print: "Contact added successfully!".
"""

def add_contact(contact_book):
    name = input()

    if name in contact_book:
        print("Contact already exists!")

    else:
        phone = input()
        email = input()
        address = input()

        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("Contact added successfully!")

        
