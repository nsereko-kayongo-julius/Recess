import tkinter as tk
from tkinter import messagebox


class ReceiptPrinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printer")

        # Create labels and entry fields
        self.label_name = tk.Label(root, text="Customer Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_items = tk.Label(root, text="Items:")
        self.label_items.pack()
        self.entry_items = tk.Entry(root)
        self.entry_items.pack()

        self.label_total = tk.Label(root, text="Total Amount:")
        self.label_total.pack()
        self.entry_total = tk.Entry(root)
        self.entry_total.pack()

        # Create print button
        self.print_button = tk.Button(
            root, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

    def print_receipt(self):
        name = self.entry_name.get()
        items = self.entry_items.get()
        total = self.entry_total.get()

        if name and items and total:
            receipt = f"Customer Name: {name}\n\nItems: {items}\n\nTotal Amount: {total}"
            messagebox.showinfo("Receipt", receipt)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")


# Create the main window
root = tk.Tk()

# Create an instance of the ReceiptPrinter class
receipt_printer = ReceiptPrinter(root)

# Run the application
root.mainloop()
