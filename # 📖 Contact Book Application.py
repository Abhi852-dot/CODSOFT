# 📖 Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
    else:
        print("\n📖 Contact List:")
        for name, details in contacts.items():
            print(f"👤 {name} | 📞 {details['phone']}")
        print()

def search_contact():
    query = input("🔍 Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if query == name or query == details["phone"]:
            print(f"\n👤 Name: {name}")
            print(f"📞 Phone: {details['phone']}")
            print(f"📧 Email: {details['email']}")
            print(f"🏠 Address: {details['address']}\n")
            found = True
            break
    if not found:
        print("⚠ Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave blank to keep current value.")
        phone = input(f"New phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email ({contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address ({contacts[name]['address']}): ") or contacts[name]['address']
        
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"✅ Contact '{name}' updated successfully!\n")
    else:
        print("⚠ Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑 Contact '{name}' deleted successfully!\n")
    else:
        print("⚠ Contact not found.\n")

def menu():
    while True:
        print("======= 📖 Contact Book =======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("👉 Choose an option (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please enter 1-6.\n")

# Run the program
menu()