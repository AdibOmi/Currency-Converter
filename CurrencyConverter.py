import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    from_curr = from_entry.get().upper()
    to_curr = to_entry.get().upper()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")
        return

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'rates' in data and to_curr in data['rates']:
            result = data['rates'][to_curr]
            result_label.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
        else:
            messagebox.showerror("Error", f"Could not convert from {from_curr} to {to_curr}")
    except:
        messagebox.showerror("Error", "Failed to connect to API")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="From Currency (e.g., USD):").pack()
from_entry = tk.Entry(root)
from_entry.pack()

tk.Label(root, text="To Currency (e.g., EUR):").pack()
to_entry = tk.Entry(root)
to_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

convert_btn = tk.Button(root, text="Convert", command=convert_currency)
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
