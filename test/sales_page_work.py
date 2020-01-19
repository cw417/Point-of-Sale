import tkinter as tk
#import home_page as hp 
#import ledger_page as lp 
#import products_page as pp 
#import totals_page as tp
import page_settings
import defs_PLUS as defs
import json
from datetime import datetime

root = tk.Tk()

# Page-specific buttons, labels, entries
l_sales = tk.Label(text="Sales")
l_sales.grid(row=0, column=0)

#e_search_item = tk.Entry(text="Type item to search: ")
#e_search_item.grid(row=1, column=0)

l_item = tk.Label(text="Enter item: ")
l_item.grid(row=2, column=0)
l_price = tk.Label(text="Enter price: ")
l_price.grid(row=3, column=0)

e_item = tk.Entry(text="Enter item: ")
e_item.grid(row=2, column=1)
e_price = tk.Entry(text="Enter price: ")
e_price.grid(row=3, column=1)


b_get_sale = tk.Button(text="Add to Sale", command=defs.get_entries_sp)
b_get_sale.grid(row=10, column=0) 


root.mainloop()



