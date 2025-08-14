import tkinter as tk
from tkinter import ttk, messagebox

# Conversion logic
def convert_temperature():
    try:
        value = float(entry_temp.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        # Convert to Celsius first
        if from_unit == "Celsius":
            c = value
        elif from_unit == "Fahrenheit":
            c = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            c = value - 273.15
        else:
            messagebox.showerror("Invalid", "Select a valid input unit.")
            return

        # Convert from Celsius to target unit
        if to_unit == "Celsius":
            converted = c
        elif to_unit == "Fahrenheit":
            converted = (c * 9/5) + 32
        elif to_unit == "Kelvin":
            converted = c + 273.15
        else:
            messagebox.showerror("Invalid", "Select a valid output unit.")
            return

        result.set(f"{value} {from_unit} = {converted:.2f} {to_unit}")
        history_listbox.insert(tk.END, f"{value} {from_unit} → {converted:.2f} {to_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric temperature.")

# Clear input and result
def clear_fields():
    entry_temp.delete(0, tk.END)
    result.set("")
    history_listbox.delete(0, tk.END)

# Main window setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("460x400")
root.resizable(False, False)

# Input label + entry
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=8)
entry_temp = tk.Entry(root, font=("Arial", 12), width=25)
entry_temp.pack()

# From Unit
from_unit_var = tk.StringVar(value="Celsius")
tk.Label(root, text="From Unit:", font=("Arial", 12)).pack(pady=5)
from_menu = ttk.Combobox(root, textvariable=from_unit_var,
                         values=["Celsius", "Fahrenheit", "Kelvin"],
                         state="readonly", font=("Arial", 12))
from_menu.pack()

# To Unit
to_unit_var = tk.StringVar(value="Fahrenheit")
tk.Label(root, text="To Unit:", font=("Arial", 12)).pack(pady=5)
to_menu = ttk.Combobox(root, textvariable=to_unit_var,
                       values=["Celsius", "Fahrenheit", "Kelvin"],
                       state="readonly", font=("Arial", 12))
to_menu.pack()

# Convert + Clear Buttons
tk.Button(root, text="Convert", command=convert_temperature,
          font=("Arial", 12), bg="green", fg="white").pack(pady=10)

tk.Button(root, text="Clear", command=clear_fields,
          font=("Arial", 12), bg="red", fg="white").pack()

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 13), fg="blue").pack(pady=10)

# History label + list
tk.Label(root, text="Conversion History:", font=("Arial", 12)).pack(pady=5)
history_listbox = tk.Listbox(root, width=50, height=6, font=("Arial", 10))
history_listbox.pack()

# Run the GUI
if __name__ == "__main__":
    root.mainloop()
