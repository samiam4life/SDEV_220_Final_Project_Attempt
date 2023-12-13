import tkinter as tk
import sqlite3
from classes import Inventory
import database

database.setup_database()

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

        self.inventory = Inventory()

        self.product_info_label = tk.Label(root, text="Product Information:")
        self.product_info_label.pack()

        # Product Name Entry
        self.product_name_label = tk.Label(root, text="Product Name:")
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.pack()

        # Product Quantity Entry
        self.product_quantity_label = tk.Label(root, text="Product Quantity:")
        self.product_quantity_label.pack()
        self.product_quantity_entry = tk.Entry(root)
        self.product_quantity_entry.pack()

        self.product_display = tk.Text(root, height=10, width=40)
        self.product_display.pack()

        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Product", command=self.remove_product)
        self.remove_button.pack()

        self.update_button = tk.Button(root, text="Update Quantity", command=self.update_quantity)
        self.update_button.pack()

        self.refresh_product_display()

    def add_product(self):
        product_name = self.product_name_entry.get()
        product_quantity = int(self.product_quantity_entry.get())

        self.cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (product_name, product_quantity))
        self.conn.commit()

        self.refresh_product_display()

    def remove_product(self):
        selected_product = self.product_display.get(tk.SEL_FIRST, tk.SEL_LAST)

        if selected_product:
            item_id = int(selected_product.split(':')[1].split(',')[0])
        
            self.cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
            self.conn.commit()

            self.refresh_product_display()

    def update_quantity(self):
        selected_product = self.product_display.get(tk.SEL_FIRST, tk.SEL_LAST)
        
        if selected_product:
            item_id = int(selected_product.split(':')[1].split(',')[0])

            new_quantity = int(self.product_quantity_entry.get())

            self.cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
            self.conn.commit()

            self.refresh_product_display

    def refresh_product_display(self):
        self.cursor.execute("SELECT * FROM items")
        products = self.cursor.fetchall()
    
        self.product_display.delete(1.0, tk.END)

        for product in products:
            self.product_display.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}\n")

    def __del__(self):
        self.conn.close()

root = tk.Tk()
app = InventoryGUI(root)

root.mainloop() 
