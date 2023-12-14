import tkinter as tk 
import sqlite3
from classes import Inventory, Notification
import database
from tkinter import simpledialog

database.setup_database()

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

        self.inventory = Inventory()
        self.inventory.update_inventory_from_database()


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

        # Product Display (Listbox)
        self.product_display = tk.Listbox(root, height=10, width=40)
        self.product_display.pack()
        self.product_display.bind('<<ListboxSelect>>', self.on_select)  # Binds selection event

        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Product", command=self.remove_product)
        self.remove_button.pack()

        self.update_button = tk.Button(root, text="Update Quantity", command=self.update_quantity_prompt)
        self.update_button.pack()

        self.refresh_product_display()

    def update_quantity_prompt(self):
        selected_product = self.product_display.get(tk.ANCHOR)
        if selected_product:
            self.get_new_quantity(selected_product)

    def get_new_quantity(self, selected_product):
        dialog = tk.Toplevel(self.root)
        dialog.title("New Quantity")

        label = tk.Label(dialog, text="Enter new quantity:")
        label.pack()

        entry = tk.Entry(dialog)
        entry.pack()

        def on_okay():
            new_quantity = entry.get()
            if new_quantity.isdigit():
                item_id = int(selected_product.split(':')[1].split(',')[0])
                new_quantity = int(new_quantity)
            
                # Update the database directly
                self.cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
                self.conn.commit()
            
                # Refresh the product display
                self.refresh_product_display()
            
                dialog.destroy()
            else:
                label.config(text="Please enter a valid integer value")

        okay_button = tk.Button(dialog, text="Okay", command=on_okay)
        okay_button.pack()

    def on_select(self, event):
        selected_index = self.product_display.curselection()
        if selected_index:
            selected_product = self.product_display.get(selected_index)
            item_id = int(selected_product.split(':')[1].split(',')[0])
            print(f'Selected product is {selected_product}') # Debugging



    def add_product(self):
        product_name = self.product_name_entry.get()
        product_quantity = int(self.product_quantity_entry.get())

        self.cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (product_name, product_quantity))
        self.conn.commit()

        last_row_id = self.cursor.lastrowid

        threshold = product_quantity * 0.34 # Threshold is set for 34% of the original quantity

        self.cursor.execute("UPDATE items SET threshold = ? WHERE id = ?", (threshold, last_row_id))
        self.conn.commit()

        self.refresh_product_display()

    def remove_product(self):
        selected_index = self.product_display.curselection()
        if selected_index:  # Check if any item is selected
            item_id = int(self.product_display.get(selected_index[0]).split(':')[1].split(',')[0])
            print(f"Item ID to delete: {item_id}")  # Debugging check

            delete_query = f"DELETE FROM items WHERE id = {item_id}" # Debugging check
            print(f"Executing query: {delete_query}") # Debugging check

            try:
                self.cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
                self.conn.commit()
                print("Deletion successful!")  # Debugging check
            except Exception as e:
                print(f"Deletion failed: {e}")  # Debugging check

            self.refresh_product_display()
        else:
            print("Please select an item to remove.")

    def update_quantity(self):
        selected_product = self.product_display.get(tk.ANCHOR)
        if selected_product:
            item_id = int(selected_product.split(':')[1].split(',')[0])

            new_quantity_str = self.product_quantity_entry.get()
            if new_quantity_str:
                new_quantity = int(new_quantity_str)

                self.cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
                self.conn.commit()

                self.refresh_product_display()

            # Fetch threshold from the database based on item ID
                threshold = None
                self.cursor.execute("SELECT threshold FROM items WHERE id = ?", (item_id,))
                result = self.cursor.fetchone()
                if result:
                    threshold = result[0]

                if threshold is not None and new_quantity < threshold:
                    product_name = selected_product.split(':')[2].split(',')[0].strip()
                    notification = Notification()
                    notification.send_notification(product_name, new_quantity, threshold)

    def refresh_product_display(self):
        self.cursor.execute("SELECT * FROM items")
        products = self.cursor.fetchall()
    
        self.product_display.delete('0', 'end')

        print(products)
        for product in products:
            self.product_display.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}\n")

    def __del__(self):
        self.conn.close()

root = tk.Tk()
app = InventoryGUI(root)

root.mainloop() 
