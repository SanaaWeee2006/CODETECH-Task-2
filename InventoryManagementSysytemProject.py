import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class InventoryManager:
    def __init__(self):
        self.products = {}  # Stores product details
        self.users = {"admin": "password"}  # Simple user authentication
        self.current_user = None

    def authenticate_user(self, username, password):
        return self.users.get(username) == password

    def add_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            return f"Product ID {product_id} already exists."
        self.products[product_id] = {"name": name, "quantity": quantity, "price": price}
        return f"Product {name} added successfully."

    def edit_product(self, product_id, name=None, quantity=None, price=None):
        if product_id not in self.products:
            return f"Product ID {product_id} does not exist."
        if name:
            self.products[product_id]["name"] = name
        if quantity is not None:
            self.products[product_id]["quantity"] = quantity
        if price is not None:
            self.products[product_id]["price"] = price
        return f"Product ID {product_id} updated successfully."

    def delete_product(self, product_id):
        if product_id not in self.products:
            return f"Product ID {product_id} does not exist."
        del self.products[product_id]
        return f"Product ID {product_id} deleted successfully."

    def generate_low_stock_report(self, threshold):
        low_stock_items = {pid: details for pid, details in self.products.items() if details["quantity"] < threshold}
        return low_stock_items

    def generate_sales_summary(self):
        return {pid: details for pid, details in self.products.items() if details["quantity"] > 0}

# GUI Implementation
class InventoryGUI:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.root.title("Inventory Management System")
        self.root.geometry("600x400")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.initialize_login()

    def initialize_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        tk.Entry(self.root, textvariable=self.username).pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        tk.Entry(self.root, textvariable=self.password, show="*").pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if self.manager.authenticate_user(username, password):
            self.manager.current_user = username
            self.initialize_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def initialize_main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Inventory Management System", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Add Product", command=self.add_product_screen).pack(pady=5)
        tk.Button(self.root, text="Edit Product", command=self.edit_product_screen).pack(pady=5)
        tk.Button(self.root, text="Delete Product", command=self.delete_product_screen).pack(pady=5)
        tk.Button(self.root, text="Generate Low Stock Report", command=self.low_stock_report).pack(pady=5)
        tk.Button(self.root, text="Generate Sales Summary", command=self.sales_summary).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.initialize_login).pack(pady=10)

    def add_product_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Product", font=("Arial", 16)).pack(pady=10)

        product_id = tk.StringVar()
        name = tk.StringVar()
        quantity = tk.IntVar()
        price = tk.DoubleVar()

        tk.Label(self.root, text="Product ID").pack()
        tk.Entry(self.root, textvariable=product_id).pack(pady=5)

        tk.Label(self.root, text="Name").pack()
        tk.Entry(self.root, textvariable=name).pack(pady=5)

        tk.Label(self.root, text="Quantity").pack()
        tk.Entry(self.root, textvariable=quantity).pack(pady=5)

        tk.Label(self.root, text="Price").pack()
        tk.Entry(self.root, textvariable=price).pack(pady=5)

        tk.Button(self.root, text="Add", command=lambda: self.add_product_action(product_id, name, quantity, price)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.initialize_main_menu).pack(pady=5)

    def add_product_action(self, product_id, name, quantity, price):
        result = self.manager.add_product(product_id.get(), name.get(), quantity.get(), price.get())
        messagebox.showinfo("Add Product", result)

    def edit_product_screen(self):
        self.clear_frame()
        # Implementation omitted for brevity

    def delete_product_screen(self):
        self.clear_frame()
        # Implementation omitted for brevity

    def low_stock_report(self):
        self.clear_frame()
        # Implementation omitted for brevity

    def sales_summary(self):
        self.clear_frame()
        # Implementation omitted for brevity

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    manager = InventoryManager()
    root = tk.Tk()
    gui = InventoryGUI(root, manager)
    root.mainloop()
