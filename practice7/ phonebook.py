# PhoneBook application using PostgreSQL

import csv
import psycopg2
from config import *

# Connect to database
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()


# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
connection.commit()


# Import contacts from CSV
def import_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute(
                """
                INSERT INTO contacts(name, phone)
                VALUES (%s, %s)
                """,
                (row["name"], row["phone"])
            )

    connection.commit()
    print("Contacts imported successfully.")


# Add new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cursor.execute(
        """
        INSERT INTO contacts(name, phone)
        VALUES (%s, %s)
        """,
        (name, phone)
    )

    connection.commit()
    print("Contact added.")


# Show all contacts
def show_contacts():
    cursor.execute("SELECT * FROM contacts")

    contacts = cursor.fetchall()

    print("\n--- CONTACT LIST ---")

    for contact in contacts:
        print(contact)


# Search contact
def search_contact():
    keyword = input("Enter name or phone: ")

    cursor.execute(
        """
        SELECT * FROM contacts
        WHERE name ILIKE %s
        OR phone ILIKE %s
        """,
        ('%' + keyword + '%', '%' + keyword + '%')
    )

    results = cursor.fetchall()

    if results:
        print("\nFound contacts:")
        for contact in results:
            print(contact)
    else:
        print("No contacts found.")


# Update contact
def update_contact():
    old_name = input("Contact name: ")

    new_name = input("New name: ")
    new_phone = input("New phone: ")

    cursor.execute(
        """
        UPDATE contacts
        SET name=%s,
            phone=%s
        WHERE name=%s
        """,
        (new_name, new_phone, old_name)
    )

    connection.commit()

    print("Contact updated.")


# Delete contact
def delete_contact():
    keyword = input("Enter name or phone: ")

    cursor.execute(
        """
        DELETE FROM contacts
        WHERE name=%s
        OR phone=%s
        """,
        (keyword, keyword)
    )

    connection.commit()

    print("Contact deleted.")


# Main menu
while True:

    print("\n===== PHONEBOOK =====")
    print("1. Import contacts from CSV")
    print("2. Add contact")
    print("3. Show contacts")
    print("4. Search contact")
    print("5. Update contact")
    print("6. Delete contact")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        import_csv("contacts.csv")

    elif choice == "2":
        add_contact()

    elif choice == "3":
        show_contacts()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        update_contact()

    elif choice == "6":
        delete_contact()

    elif choice == "0":
        break

    else:
        print("Invalid option.")

cursor.close()
connection.close()