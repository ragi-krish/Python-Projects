
import os
#from tabulate import tabulate
from openpyxl import Workbook


# This gets the directory where the current Python file is saved
base_path = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(base_path, "contacts.txt")


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    with open(FILENAME, "a") as file:
        file.write(f"{name},{phone}\n")
    print("Contact added successfully!")

def view_contacts():
    print("\n--- All Contacts ---")
    #table = []

    try:
        with open(FILENAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts available.")
                return
            for line in contacts:
                name, phone = line.strip().split(",")
                
                print(f"Name: {name}, Phone: {phone}")

                #table.append([name, phone])
        #print(tabulate(table, headers=["Name", "Phone"], tablefmt="grid"))
    except FileNotFoundError:
        print("Contact file not found.")

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                if name.lower() == search_name:
                    print(f"Found - Name: {name}, Phone: {phone}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")

def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    updated_contacts = []
    found = False
    try:
    # Open the contact file in read mode
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")  # split each line into name and phone

            # If the name does not match the one to delete, keep the contact
                if name.lower() != delete_name:
                    updated_contacts.append(line)
                else:
                    found = True  # We found the contact to delete

        if found:
        # Now rewrite the file without the deleted contact
            with open(FILENAME, "w") as file:
                file.writelines(updated_contacts)  # write the updated list back to the file
            print("Contact deleted.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")


def update_contact():
    update_name = input("Enter name to update phone number: ").strip().lower()
    updated_contacts = []
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                if name.lower() == update_name:
                    new_phone = input("Enter new phone number: ").strip()
                    updated_contacts.append(f"{name},{new_phone}\n")
                    found = True
                else:
                    updated_contacts.append(line)

        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_contacts)
            print("Contact updated.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")


def export_to_excel():
    # Get the current directory of the script
    excel_file_path = os.path.join(base_path, "contacts.xlsx")
    
    try:
        with open(FILENAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts to export.")
                return
            
            wb = Workbook()
            ws = wb.active
            ws.title = "Contacts"
            
            # Add header
            ws.append(["Name", "Phone"])

            # Add contacts
            for line in contacts:
                name, phone = line.strip().split(",")
                ws.append([name, phone])
            
            # Save Excel file
            wb.save(excel_file_path)
            print(f"Contacts exported successfully to {excel_file_path}")
    except FileNotFoundError:
        print("No contacts file found to export.")


# --- Main Menu ---
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Export to Excel")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        export_to_excel()
    elif choice == "7":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid option. Please choose again.")
