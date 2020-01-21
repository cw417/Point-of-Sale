from datetime import datetime
import tkinter as tk
import pandas as pd
import defs as defs
import json

class SalesTracker(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    def init_window(self):
  
        self.master.title("Sales Tracker")
        
        self.pack(fill=tk.BOTH, expand=1)

        label_width = 20
        entry_width = 60
        button_width = label_width

        # Create Labels for entry fields
        l_item = tk.Label(self, width=label_width, text="Item: ")
        l_price = tk.Label(self, width=label_width, text="Price: ")

        # Create entry fields
        e_item = tk.Entry(self, width=entry_width)
        e_price = tk.Entry(self, width=entry_width)

        # Create submit button
        b_sub = tk.Button(self, width=button_width, text="Submit", command=lambda: print(get_entries()))
        b_quit = tk.Button(self, width=button_width, text="Close", command=root.quit)

        # Set up layout of label fields
        l_item.grid(row=0, column=0, sticky='w')
        l_price.grid(row=1, column=0, sticky='w')

        # Set up layout of entry fields
        e_item.grid(row=0, column=1)
        e_price.grid(row=1, column=1)

        # Set button layout
        # Starts at 10 to enable later addition of extra entry fields
        b_sub.grid(row=10, column=0)
        b_quit.grid(row=11, column=0)


        def get_entries():
            # Returns entry fields and creates items list, 
            # prices list, and current_sale dictionary

            items = []
            prices = []
            current_sale = {}

            item = e_item.get()
            items.append(item)
            price = e_price.get()
            prices.append(price)

            current_sale.update({"items": items})
            current_sale.update({"prices": prices})

            return items, prices, current_sale


root = tk.Tk()

root.geometry("600x95")

app = SalesTracker(root)
root.mainloop()

