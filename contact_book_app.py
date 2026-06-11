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

    
"""
Create a function named view_contact that displays details of a specific contact.

Your function should:

Take a contact book dictionary as a parameter
Get a contact name from user input (using input())
Display the contact's details if found
Print "Contact not found!" if the contact doesn't exist
When displaying a contact, use this exact format:

Name: [name]
Phone: [phone]
Email: [email]
Address: [address]

Example:
If the contact book contains Alice's information and the user enters "Alice", output:

Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St
If the user enters "Bob" (who doesn't exist), output:

Contact not found!
Note: Your function should only output the contact details or the error message
 - no additional prompting text.
"""

def view_contact(contact_book):
    contact_to_view = input()

    if contact_to_view in contact_book:
        contact = contact_book[contact_to_view]

        print(f"Name: {contact_to_view}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        
    else:
        print("Contact not found!")


"""
The next step is to create the edit_contact function.
This function will allow users to update the details of
an existing contact in the Contact Book.

Your Task:
Create a function named edit_contact that takes one argument:
contact_book (a dictionary).
Get input for the contact's name that the user wants to edit.
Check if the name exists in the contact_book:
If it exists, prompt the user to input new values for the contact's phone, email,
and address (in that order!).
If the user provides no input (presses Enter), keep the current value for
that field (in this case the input will be an empty string, '').
Update the contact's information in the dictionary.
Print: "Contact updated successfully!".
If the contact does not exist, print: "Contact not found!".

Remember: Only read inputs for phone, email, and address if the contact exists
in the contact book. If the contact is not found, print the error
message immediately without trying to read additional inputs.

Expected Behavior:
For a contact_book containing:

{"Alice": {"phone": "123-456-7890", "email": "alice@example.com", 
"address": "123 Main St"}}
If the user enters:

Alice
987-654-3210

456 Elm St
The updated contact_book should look like this:

{"Alice": {"phone": "987-654-3210", "email": "alice@example.com",
"address": "456 Elm St"}}
If the user enters a name that does not exist:

Bob
The output should be:

Contact not found!
"""

def edit_contact(contact_book: dict):
    contact_to_edit = input()
    
    if contact_to_edit not in contact_book:
        print("Contact not found!")
        return

    elif contact_to_edit in contact_book:
        contact = contact_book[contact_to_edit]

        new_phone = input()
        new_email = input()
        new_address = input()
        
        if new_phone:   # if new_phone == "" --> False, podmínka se neprovede
            contact["phone"] = new_phone

        if new_email:
            contact["email"] = new_email   

        if new_address:
            contact["address"] = new_address

        print("Contact updated successfully!")


"""
The next step is to create the delete_contact function.
This function will allow users to remove a specific contact from the Contact Book.

Your Task:
Create a function named delete_contact that takes one argument:
contact_book (a dictionary).
Get input for the contact's name that the user wants to delete.
Check if the name exists in the contact_book:
If it exists, remove the contact from the dictionary.
Print: "Contact deleted successfully!".
If the contact does not exist, print: "Contact not found!".
"""

def delete_contact(contact_book: dict):
    contact_to_delete = input()

    if contact_to_delete not in contact_book:
        print("Contact not found!")
        return
    
    elif contact_to_delete in contact_book:
        del contact_book[contact_to_delete]
        print("Contact deleted successfully!")

