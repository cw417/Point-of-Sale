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

        def get_entries():
            """This function gets entries from the fields and returns them
            as a dictionary when the submit button is pressed"""
            dict = {}


            total = e_total.get()
            dict.update({'total': total})
            pay_type = e_pay_type.get()
            dict.update({'pay_type': pay_type})

            dict_json = json.dump(dict, open("sales.json", 'a'), indent=4, sort_keys=True)
            dict_csv = defs.pd_check(total, pay_type, 'sales.csv')
            
        # Create Labels for entry fields
        l_total = tk.Label(self, width=label_width, text="Sale Total: ")
        l_pay_type = tk.Label(self, width=label_width, text="Payment Type: ")

        # Create entry fields
        e_total = tk.Entry(self, width=entry_width)
        e_pay_type = tk.Entry(self, width=entry_width)

        # Create submit button
        b_sub = tk.Button(self, width=button_width, text="Submit", command=lambda:[get_entries(), root.quit()])

        # Set up layout of label fields
        l_total.grid(row=0, column=0, sticky='w')
        l_pay_type.grid(row=1, column=0, sticky='w')

        # Set up layout of entry fields
        e_total.grid(row=0, column=1)
        e_pay_type.grid(row=1, column=1)

        # Set button layout
        # Starts at 10 to enable later addition of extra entry fields
        b_sub.grid(row=10, column=0)

root = tk.Tk()

root.geometry("600x70")

app = SalesTracker(root)
root.mainloop()

