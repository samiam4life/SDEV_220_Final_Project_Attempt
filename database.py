import sqlite3 

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

def setup_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

def add_item(name, quantity):
    cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()

def update_quantity(item_id, new_quantity):
    cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
    conn.commit()

def get_items():
    cursor.execute("SELECT * FROM items")
    return cursor.fetchall()

def delete_item(item_id):
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id))
    conn.commit()

