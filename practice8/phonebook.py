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


# Upsert contact (insert or update)
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cursor.execute(
        "CALL upsert_contact(%s, %s)",
        (name, phone)
    )

    connection.commit()

    print("Contact added or updated.")


# Show all contacts
def show_contacts():
    cursor.execute("SELECT * FROM contacts")

    contacts = cursor.fetchall()

    print("\n--- CONTACT LIST ---")

    for contact in contacts:
        print(contact)


# Search using SQL function
def search_contact():
    pattern = input("Enter pattern: ")

    cursor.execute(
        "SELECT * FROM get_contacts_by_pattern(%s)",
        (pattern,)
    )

    contacts = cursor.fetchall()

    if contacts:
        print("\nFound contacts:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


# Pagination
def show_page():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cursor.execute(
        "SELECT * FROM get_contacts_page(%s, %s)",
        (limit, offset)
    )

    rows = cursor.fetchall()

    if rows:
        print("\nContacts:")
        for row in rows:
            print(row)
    else:
        print("No contacts.")


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


# Delete using stored procedure
def delete_contact():
    value = input("Enter name or phone: ")

    cursor.execute(
        "CALL delete_contact(%s)",
        (value,)
    )

    connection.commit()

    print("Contact deleted.")


# Bulk insert using procedure
def insert_many():
    names = ["Ali", "Bob", "Tom"]
    phones = ["87001234567", "123", "87770001122"]

    cursor.execute(
        "CALL insert_many(%s,%s)",
        (names, phones)
    )

    connection.commit()

    print("Bulk insert completed.")


# Main menu
while True:

    print("\n===== PHONEBOOK =====")
    print("1. Import contacts from CSV")
    print("2. Add contact (Upsert)")
    print("3. Show all contacts")
    print("4. Search by pattern")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Show page")
    print("8. Insert many")
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

    elif choice == "7":
        show_page()

    elif choice == "8":
        insert_many()

    elif choice == "0":
        break

    else:
        print("Invalid option.")

cursor.close()
connection.close()