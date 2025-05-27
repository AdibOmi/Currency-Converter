# A simple currency converter using Frankfurter API
#cuz this API is free

#using tkinter for gui
import tkinter as tk
from tkinter import messagebox
#in terminal, run this-> pip install requests
import requests

def convert_func():
    #conv_from -> currency to convert from. Same for conv_to
    #inp_from -> input given in gui for "from", inp_to -> the one to be converted to
    #these are not built in, but declared later in the code
    conv_from = inp_from.get().upper() 
    #converting to upper case after fetching from input box
    conv_to = inp_to.get().upper()

    try:
        #amount, amount_entered are declared later as well
        amount =  float(amount_entered.get())
    except:
        #showerror gives a pop-up error message similar to JS alert
        messagebox.showerror("Invalid Input")
        return

    #connecting the api
    #link from web: https://api.frankfurter.dev/v1/latest
    url = f"https://api.frankfurter.dev/v1/latest?amount={amount}&from={conv_from}&to={conv_to}"
    # ? indicates everything after ? are parameters
    #this is how the apis are connected. An example to be more clear:
    #url = f"https://api.frankfurter.dev/v1/latest?amount=100&from=USD&to=BDT

    try:
        #response,  data_from_api, these are variables, not built in
        response= requests.get(url)
        #fetches the latest exchange rate
        data_from_api=response.json()
        #converts the response into python readable format
    
        if 'rates' in data_from_api and conv_to in data_from_api['rates']:

        # this line checks if data has a rates section,
        # and if the rates section have our goal currency 
            result= data_from_api['rates'][conv_to]
            #fetches that rate from rates section
            rounded_value=round(result, 2)
            #2 decimal places
            result_label.config(text=f"{amount} {conv_from} = {rounded_value} {conv_to}")
            #config is used to update already created labels
            #:.2f means 2 digits after decimal
        else:
            messagebox.showerror("Error")    
    except:
        messagebox.showerror("Failed to connect API")



# Setting up the GUI 

root = tk.Tk()
#creates main app window, and root is a random var
root.title(("Currency Converter"))
tk.Label(root, text="Convert From (e.g: USD)").pack()
#pack() is used to place label vertically
#Label() is a built in Tkinter
inp_from=tk.Entry(root)
inp_from.pack()
#declaring the variables we used at the start
#Entry() creates a text input box
tk.Label(root, text="Convert To (e.g: EUR)").pack()
inp_to=tk.Entry(root)
inp_to.pack()

tk.Label(root, text="Amount").pack()
amount_entered=tk.Entry(root)
amount_entered.pack()

convert_btn=tk.Button(root, text="Convert", command=convert_func)
#button to call the function
convert_btn.pack(pady=10)
#pady=10 adds vertical padding. Experiment with these

result_label=tk.Label(root, text="", font=("Arial", 12))
result_label.pack()
#created the var that we used before

root.mainloop()
#keeps window open and responsive