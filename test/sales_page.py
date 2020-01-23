from datetime import datetime
import tkinter as tk
import home_page as hp 
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings
import json
import os

# WORKFLOW
# entry fields for item, price --> .get() and append to items, prices lists with "Add to Sale" 
# create dictionary with items, prices, and datetime
# make dict into pandas df
# save df as csv file
# read from csv to get totals


#TO DO: 
# Make Total button to display totals
# "New Sale" button to clear current_sale.csv
# Figure out how to track idividual sales and organize into days


class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.items = []
            self.prices = []

            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_sales.grid(row=0, column=0)

            l_item1 = tk.Label(self, text="Item: ")
            l_item1.grid(row=2, column=0)
            l_price1 = tk.Label(self, text="Price: ")
            l_price1.grid(row=3, column=0)

            # Entry fields for item & price
            self.e_item = tk.Entry(self, text="item1")
            self.e_item.grid(row=2, column=1)
            self.e_price = tk.Entry(self, text="price1")
            self.e_price.grid(row=3, column=1)
            
            items = []
            prices = []
            current_sale = {}

            def get_entries():
                # Dumps entries to json file to be used by current_sale
                item = self.e_item.get()
                items.append(item)
                price = self.e_price.get()
                self.items.append(item)
                self.prices.append(price)
                print(f"Added items: {item}, ${price}")
                self.e_item.delete(0, tk.END)
                self.e_price.delete(0, tk.END)

                
            # Buttons for page functions
            b_add_to_sale = tk.Button(self, text="Add to Sale", command=lambda: get_entries())
            #b_get_total = tk.Button(self, text="Get Total", command=lambda: )
            b_add_to_sale.grid(row=10, column=0)
            #b_get_total.grid(row=11, column=0)

            # Buttons for page selection
            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.SalesLedger))
            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_home_page.grid(row=20, column=11)
            b_ledger.grid(row=20, column=12)            
            b_products_page.grid(row=20, column=13)
            b_totals_page.grid(row=20, column=14)
