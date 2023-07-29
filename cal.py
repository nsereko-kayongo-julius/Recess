import tkinter as tk
from tkinter import messagebox


class RestaurantReceiptPrinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Nsereko julius Restaurant Receipt Printer")
        self.root.geometry("370x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5F5F5")

        # Create labels and entry fields
        self.label_name = tk.Label(
            root, text="Customer Name:", font="arial 10 bold", bg="#F5F5F5")
        self.label_name.place(x=10, y=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.place(x=140, y=10)

        self.label_items = tk.Label(
            root, text="Items:", font="arial 10 bold", bg="#F5F5F5")
        self.label_items.place(x=10, y=30)
        self.entry_items = tk.Entry(root)
        self.entry_items.place(x=140, y=30)

        self.label_total = tk.Label(

            root, text="Total Amount:", font="arial 10 bold", bg="#F5F5F5")
        self.label_total.place(x=10, y=50)
        self.entry_total = tk.Entry(root)
        self.entry_total.place(x=140, y=50)

        # Create print button
        self.print_button = tk.Button(
            root, text="Print Receipt", command=self.print_receipt, bg="green", fg="white")
        self.print_button.place(x=140, y=100)

        # Create exit button
        self.exit_button = tk.Button(
            root, text="Exit", command=self.exit_program)
        self.exit_button.place(x=240, y=100)

        # Create receipt frame
        self.receipt_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        self.receipt_frame.place(x=40, y=200)

    def print_receipt(self):
        heading = '---------RECIEPT----------'
        name = self.entry_name.get()
        items = self.entry_items.get()
        total = self.entry_total.get()

        if name and items and total:
            receipt = f"{heading}\n\nCustomer Name: {name}\n\nItems: {items}\n\nTotal Amount: {total}\n\nNote:\nonce goods are sold are not returnable"

            # Clear previous receipt if any
            for widget in self.receipt_frame.winfo_children():
                widget.destroy()

            # Display receipt in the frame
            receipt_label = tk.Label(
                self.receipt_frame, text=receipt, justify="left", bg="white")
            receipt_label.pack(anchor="w")
        else:
            self.show_error("Error", "Please fill in all fields.")

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def exit_program(self):
        self.root.quit()


# Create the main window
root = tk.Tk()

# Create an instance of the ReceiptPrinter class
receipt_printer = RestaurantReceiptPrinter(root)

# Run the application
root.mainloop()
