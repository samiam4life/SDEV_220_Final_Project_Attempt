# Created three classes to handle inventory management
# Will need to integrate the GUI with these inventory management classes

# Product class - methods: getters and setters for attributes, methods to update quantity, check if low on stock

# Inventory class - manages collection of Product instances - methods: add products, remove products, update product quantity

# Notification class - handles notification mechanism for low inventory levels - methods: send notification alert

class Product():
    def __init__(self, name, id, quantity, threshold):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.threshold = threshold

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - Quantity: {self.quantity}, Threshold: {self.threshold}"

    # Methods for managing product details

dice = Product("Dice", "DICE001", 50, 10)
minis = Product("Minis", "MINI002", 20, 5)
board_games = Product("Board Games", "BOARD003", 15, 3)


class Inventory():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                break
        else:
            print(f"Product with ID {id} not found in inventory.")

    def update_quantity(self, id, new_quantity):
        for product in self.products:
            if product.id == id:
                product.quantity = new_quantity
                break
        else:
            print(f"Product with ID {id} not found in inventory.")

    def display_inventory(self):
        for product in self.products:
            print(product)

    # Methods for managing the inventory


class Notification():
    def __init__(self):
        pass

    def send_notification(self, product_name, current_quantity, threshold):
        if current_quantity < threshold:
            message = f"Inventory for {product_name} is low! Current amount: {current_quantity}"
            # Add code for GUI alert
        else: 
            print("Quantity is above threshold.")


# GUI Tkinter integration
# Set up GUI elements and connect to inventory classes

if __name__ == "__main__":
    pass
    # Initialize inventory, notification, and GUI
    # Set up event handlers to manage interactions between GUI and inventory classes
    # Start GUI application loop



