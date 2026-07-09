import psycopg2
import json
import csv

from config import *

# ==========================
# CONNECT TO DATABASE
# ==========================

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()

# ==========================
# ADD CONTACT
# ==========================

def add_contact():

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO contacts(name,email,birthday)
        VALUES(%s,%s,%s)
    """, (name,email,birthday))

    connection.commit()

    print("Contact added.")

# ==========================
# ADD PHONE
# ==========================

def add_phone():

    name = input("Contact name: ")

    phone = input("Phone: ")

    phone_type = input("Type (home/work/mobile): ")

    cursor.execute(
        "CALL add_phone(%s,%s,%s)",
        (name,phone,phone_type)
    )

    connection.commit()

    print("Phone added.")

# ==========================
# SHOW CONTACTS
# ==========================

def show_contacts():

    cursor.execute("""

    SELECT

    c.name,
    c.email,
    c.birthday,
    p.phone,
    p.type,
    g.name

    FROM contacts c

    LEFT JOIN phones p
    ON c.id=p.contact_id

    LEFT JOIN groups_table g
    ON c.group_id=g.id

    ORDER BY c.name

    """)

    rows = cursor.fetchall()

    print()

    for row in rows:
        print(row)

# ==========================
# SEARCH CONTACTS
# ==========================

def search_contact():

    keyword = input("Search: ")

    cursor.execute(
        "SELECT * FROM search_contacts(%s)",
        (keyword,)
    )

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Nothing found.")
        return

    print()

    for row in rows:
        print(row)

# ==========================
# MOVE TO GROUP
# ==========================

def move_to_group():

    name = input("Contact name: ")

    group = input("New group: ")

    cursor.execute(
        "CALL move_to_group(%s,%s)",
        (name, group)
    )

    connection.commit()

    print("Contact moved.")

# ==========================
# FILTER BY GROUP
# ==========================

def filter_group():

    group = input("Group: ")

    cursor.execute("""

    SELECT

    c.name,
    c.email,
    c.birthday,
    p.phone,
    p.type

    FROM contacts c

    JOIN groups_table g
    ON c.group_id=g.id

    LEFT JOIN phones p
    ON c.id=p.contact_id

    WHERE g.name=%s

    """,(group,))

    rows = cursor.fetchall()

    if len(rows)==0:
        print("No contacts.")
        return

    print()

    for row in rows:
        print(row)

# ==========================
# SORT CONTACTS
# ==========================

def sort_contacts():

    print()

    print("1 - Sort by name")
    print("2 - Sort by birthday")
    print("3 - Sort by date added")

    choice = input()

    if choice=="1":

        sql="""

        SELECT * FROM contacts
        ORDER BY name

        """

    elif choice=="2":

        sql="""

        SELECT * FROM contacts
        ORDER BY birthday

        """

    else:

        sql="""

        SELECT * FROM contacts
        ORDER BY id

        """

    cursor.execute(sql)

    rows=cursor.fetchall()

    print()

    for row in rows:
        print(row)

# ==========================
# EXPORT JSON
# ==========================

def export_json():

    cursor.execute("""

    SELECT

    c.name,
    c.email,
    c.birthday,
    p.phone,
    p.type,
    g.name

    FROM contacts c

    LEFT JOIN phones p
    ON c.id=p.contact_id

    LEFT JOIN groups_table g
    ON c.group_id=g.id

    ORDER BY c.id

    """)

    rows = cursor.fetchall()

    data = []

    for row in rows:

        data.append({

            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "phone": row[3],
            "type": row[4],
            "group": row[5]

        })

    with open("contacts.json","w",encoding="utf-8") as file:

        json.dump(data,file,indent=4)

    print("JSON exported.")

# ==========================
# IMPORT JSON
# ==========================

def import_json():

    with open("contacts.json","r",encoding="utf-8") as file:

        data=json.load(file)

    for person in data:

        cursor.execute("""

        SELECT id

        FROM contacts

        WHERE name=%s

        """,(person["name"],))

        exists=cursor.fetchone()

        if exists:

            answer=input(f'{person["name"]} already exists. Overwrite? (y/n): ')

            if answer.lower()=="y":

                cursor.execute("""

                UPDATE contacts

                SET

                email=%s,

                birthday=%s

                WHERE name=%s

                """,(person["email"],person["birthday"],person["name"]))

                contact_id=exists[0]

            else:

                continue

        else:

            cursor.execute("""

            INSERT INTO contacts(name,email,birthday)

            VALUES(%s,%s,%s)

            RETURNING id

            """,(person["name"],person["email"],person["birthday"]))

            contact_id=cursor.fetchone()[0]

        if person["group"]:

            cursor.execute("""

            SELECT id

            FROM groups_table

            WHERE name=%s

            """,(person["group"],))

            group=cursor.fetchone()

            if group is None:

                cursor.execute("""

                INSERT INTO groups_table(name)

                VALUES(%s)

                RETURNING id

                """,(person["group"],))

                group_id=cursor.fetchone()[0]

            else:

                group_id=group[0]

            cursor.execute("""

            UPDATE contacts

            SET group_id=%s

            WHERE id=%s

            """,(group_id,contact_id))

        if person["phone"]:

            cursor.execute("""

            INSERT INTO phones(contact_id,phone,type)

            VALUES(%s,%s,%s)

            """,(contact_id,person["phone"],person["type"]))

    connection.commit()

    print("JSON imported.")

# ==========================
# IMPORT CSV
# ==========================

def import_csv():

    with open("contacts.csv","r",encoding="utf-8") as file:

        reader=csv.DictReader(file)

        for row in reader:

            cursor.execute("""

            INSERT INTO contacts(name,email,birthday)

            VALUES(%s,%s,%s)

            RETURNING id

            """,(row["name"],row["email"],row["birthday"]))

            cid=cursor.fetchone()[0]

            cursor.execute("""

            INSERT INTO phones(contact_id,phone,type)

            VALUES(%s,%s,%s)

            """,(cid,row["phone"],row["type"]))
            cursor.execute(
                "CALL move_to_group(%s,%s)",
                (row["name"], row["group"])
            )

    connection.commit()

    print("CSV imported.")

# ==========================
# PAGINATION
# ==========================

def show_pages():

    limit = 5
    offset = 0

    while True:

        cursor.execute("""

        SELECT

        c.name,
        c.email,
        c.birthday

        FROM contacts c

        ORDER BY c.id

        LIMIT %s
        OFFSET %s

        """,(limit,offset))

        rows=cursor.fetchall()

        print()

        for row in rows:
            print(row)

        print()
        print("next")
        print("prev")
        print("quit")

        cmd=input("Command: ").lower()

        if cmd=="next":
            offset+=limit

        elif cmd=="prev":

            if offset>=limit:
                offset-=limit

        elif cmd=="quit":
            break
# ==========================
# MAIN MENU
# ==========================

while True:

    print()
    print("========== PHONEBOOK ==========")
    print("1. Import CSV")
    print("2. Import JSON")
    print("3. Export JSON")
    print("4. Add Contact")
    print("5. Add Phone")
    print("6. Show Contacts")
    print("7. Search")
    print("8. Filter Group")
    print("9. Move To Group")
    print("10. Sort")
    print("11. Pagination")
    print("0. Exit")

    choice=input("Choose: ")

    if choice=="1":
        import_csv()

    elif choice=="2":
        import_json()

    elif choice=="3":
        export_json()

    elif choice=="4":
        add_contact()

    elif choice=="5":
        add_phone()

    elif choice=="6":
        show_contacts()

    elif choice=="7":
        search_contact()

    elif choice=="8":
        filter_group()

    elif choice=="9":
        move_to_group()

    elif choice=="10":
        sort_contacts()

    elif choice=="11":
        show_pages()

    elif choice=="0":
        break

    else:
        print("Wrong choice.")


cursor.close()
connection.close()