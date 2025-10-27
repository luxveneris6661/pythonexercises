#personal info database in SQL with update, delete, search, import export functions

import mysql.connector 
import pandas as pd
import os

def ensure_db_exists(db_name, host, user, password):
    conn = mysql.connector.connect(
     host = host,
     user = user,
     password = password   
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    cursor.close()
    conn.close()

    
def connect_db():
    db_name = "personalinfodb" #NO COMMAS
    host = "localhost"
    user = "root"
    password = "Le$bean69"
    
    ensure_db_exists(db_name, host, user, password)

    conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password, 
        database = db_name,
        autocommit = True
    )
    return conn

       

def setup_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients(
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(100) NOT NULL,
         region VARCHAR(100) NOT NULL, 
         email VARCHAR(100) NOT NULL,
         age INT CHECK (age > 0),
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
         UNIQUE (name,email)
        ) 
    ''')

#CRUD Operations

def insert_data(cursor):
    clients = [
        ('R.A. Pink', 'Shinjuku', 'rapink@gmail.com', 35),
        ('Rai Gatts', 'Suginami', 'raigatts@gmail.com', 35),
        ('Mikka Verneaux', 'Nakano', 'mikkaverneaux@gmail.com', 34),
        ('Lucifer Veneris', 'Nakano', 'luciferveneris@gmail.com', 24),
        ('Abe Lee', 'Nakano', 'abelee@gmail.com', 26)
    ]
    cursor.executemany('''
        INSERT INTO Clients (name, region, email, age)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            region = VALUES(region),
            email = VALUES(email),
            age = VALUES(age)
    ''', clients)

def view_clients(cursor):
    cursor.execute("SELECT * FROM Clients ORDER BY id")
    for row in cursor.fetchall():
        print(row)

def search_clients(cursor, keyword):
    query = '''
    SELECT * FROM Clients
    WHERE name LIKE %s OR region LIKE %s OR email LIKE %s
    '''
    kw = f"%{keyword}%"
    cursor.execute(query, (kw, kw, kw))
    for row in cursor.fetchall():
        print(row)

def update_client(cursor, client_id, field, value):
    valid_fields = ["name", "region", "email", "age"]
    if field not in valid_fields:
        print("Invalid field name.")
        return
    query = f"UPDATE Clients SET {field} = %s WHERE id = %s"
    cursor.execute(query, (value, client_id))
    print(f"Updated Client {client_id}.")

def delete_client(cursor, client_id):
    cursor.execute("DELETE FROM Clients WHERE id = %s", (client_id,))
    print(f"Deleted Client {client_id}.")


def import_from_csv(cursor, filename):
    df = pd.read_csv(filename)
    data = [tuple(x) for x in df[['name','region','email','age']].to_records(index=False)]
    cursor.executemany('''
        INSERT INTO Clients (name, region, email, age)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            region = VALUES(region),
            email = VALUES(email),
            age = VALUES(age)
    ''', data)
    print(f"Imported {len(data)} records from {filename}.")

def export_to_csv(conn, filename="clients_export.csv"):
    save_dir = r"C:\Users\WURUOQING\Desktop\python"
    os.makedirs(save_dir, exist_ok=True)

    # Ensure the filename has .csv extension
    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    file_path = os.path.join(save_dir, filename)

    df = pd.read_sql("SELECT * FROM Clients", conn)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')

    print(f"Exported {len(df)} records to: {os.path.abspath(file_path)}")


def menu():
    print("""
==== Personal Info Manager ====
1. View all clients
2. Search client
3. Update client
4. Delete client
5. Import from CSV
6. Export to CSV
7. Exit
""")

def main():
    conn = connect_db()
    cursor = conn.cursor()
    setup_tables(cursor)
    insert_data(cursor)

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_clients(cursor)
        elif choice == "2":
            keyword = input("Enter keyword: ")
            search_clients(cursor, keyword)
        elif choice == "3":
            client_id = input("Enter client ID: ")
            field = input("Field to update (name, region, email, age): ")
            value = input("New value: ")
            update_client(cursor, client_id, field, value)
        elif choice == "4":
            client_id = input("Enter client ID to delete: ")
            delete_client(cursor, client_id)
        elif choice == "5":
            filename = input("CSV filename to import: ")
            import_from_csv(cursor, filename)
        elif choice == "6":
            filename = input("Export filename (default clients_export.csv): ") or "clients_export.csv"
            export_to_csv(conn, filename)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()


