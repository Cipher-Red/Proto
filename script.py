import sys
import sqlite3

# Connect (creates file if not exists)
conn = sqlite3.connect("Proto.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    pid TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    qty INTEGER NOT NULL,
    sale_price REAL NOT NULL,
    manufacturing_cost REAL NOT NULL
)
""")

conn.commit()

# --- Data Storage (In-memory) ---
products = {}

# --- Functions ---
def add_product():
    while True:
        if input("Do you want to continue? (y/n): ").lower() == "n":
            break
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        qty = int(input("Enter Quantity: "))
        sale_price = float(input("Enter Sale Price: "))
        man = float(input("Enter Manufacturing Cost: "))

        cursor.execute("INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?, ?)",
                       (pid, name, qty, sale_price, man))
        conn.commit()

        print("Product added\n")



def view_products():
    print("*** Product List ***")
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        pid, name, qty, sale_price, man = row
        print(f"{'-'*25}ID: {pid} - Name: {name}{'-'*25}"
              f"\nQty: {qty}"
              f"\nSale Price: ${sale_price}"
              f"\nManufacturing Cost: ${man}")


# --- Main Menu ---
def menu():
    while True:
        print("===== Proto 0.001 System =====")
        print("1. Add Product")
        print("2. View Products")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '0':
            print("Exiting...")
            conn.close()
            exit()

        else:
            print("Invalid Input!\n")

# --- Run Program ---
if __name__ == "__main__":
    menu()
