import tkinter as tk
import classes

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")

        self.inventory = Inventory()

        self.product_info_label = tk.Label(root, text="Product Information:")
        self.product_info_label.pack()

        self.product_display = tk.Text(root, height=10, width=40)
        self.product_display.pack()

        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Product", command=self.remove_product)
        self.remove_button.pack()

        self.update_button = tk.Button(root, text="Update Quantity", command=self.update_quantity)
        self.update_button.pack()

    def add_product(self):

    def remove_product(self):

    def update_quantity(self):

root = tk.Tk()
app = InventoryGUI(root)

root.mainloop()