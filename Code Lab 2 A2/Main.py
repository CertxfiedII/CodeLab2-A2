import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json

root = tk.Tk()
root.title("Currency Conversion")
root.geometry("500x400")
root.resizable(0, 0)
root.configure(background="#000000")


def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_input.get()
    to_currency = to_currency_input.get()

    try:
        # Make a request to the API
        response = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_00dKIlcSwaCIPME3BV6BeSpuec83nhWjPUjqCYfb")
        response.raise_for_status()  

        data = response.json()
        print(data)

        if response.status_code == 200:
            conversion_rate = data['data'][to_currency]
            converted_amount = round(amount * conversion_rate, 2)
            result_input.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            messagebox.showerror("Error", "Failed to retrieve conversion rates.")
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        messagebox.showerror("Error", str(e))

    conversion_rates = data.get('data', {})

    with open("conversion_rates.json", "w") as file:
        json.dump(conversion_rates, file)

def clear_fields():
    amount_entry.delete(0, tk.END)
    from_currency_input.set("")
    to_currency_input.set("")
    result_input.config(text="") 
def exit_app():
    root.destroy()

top = tk.Frame(root, bg="#566573", width=500, height=79)
top.grid()

title = tk.Label(root, text="CURRENCY RATINGS",  font=("Arial", 27, "bold"), fg="#ffffff", bg="#000000") 
title.place(x=85, y=15)

amount_label = tk.Label(root, text="Enter Amount:", font=("Arial", 12), fg="#ffffff", bg="#4d5656")
amount_label.place(x=195, y=90)
amount_entry = tk.Entry(root, width=16, font=("Arial", 12))
amount_entry.place(x=175, y=115)

from_currency_label = tk.Label(root, text="From:", font=("Arial", 12), fg="#ffffff", bg="#4d5656")
from_currency_label.place(x=55, y=155)
from_currency_input = ttk.Combobox(root, width=12, font=("Arial", 12))
from_currency_input['values'] = ['CAD', 'EUR', 'GBP', 'HKD', 'INR', 'JPY', 'KRW', 'PHP', 'USD']
from_currency_input.place(x=110, y=155)

to_currency_label = tk.Label(root, text="To:", font=("Arial", 12), fg="#ffffff", bg="#4d5656")
to_currency_label.place(x=265, y=155)
to_currency_input = ttk.Combobox(root, width=12, font=("Arial", 12))
to_currency_input['values'] = ['CAD', 'EUR', 'GBP', 'HKD', 'INR', 'JPY', 'KRW', 'PHP', 'USD']
to_currency_input.place(x=300, y=155)

convert = tk.Button(root, width=12, font=("Arial", 12), text="Convert", bg="#FFFF00", fg="#000000", command=convert_currency)
convert.place(x=190, y=210)
clear = tk.Button(root, width=12, font=("Arial", 12), text="Clear", bg="#013220", fg="#000000", command=clear_fields)
clear.place(x=190, y=250)
result_input = tk.Label(root, text="", font=("Arial", 12), fg="#ffffff", bg="#232323")
result_input.place(x=150, y=290)
exit = tk.Button(root, text="Exit", width=12, font=("Arial", 12), bg="#303234", fg="#FF0000", command=exit_app)
exit.place(x=190, y=330)



root.mainloop()