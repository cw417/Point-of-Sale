from datetime import datetime
import tkinter as tk
import home_page as hp 
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings
import pandas as pd
import json
import os

# WORKFLOW
# entry fields for item, price --> .get() and append to items, prices lists with "Add to Sale"
# "Total" button calls get_total() method to return subtotal, total 
# create dictionary with items, prices, and datetime
# make dict into pandas df
# save df as csv file
# read from csv to get totals


#TO DO: 
# "New Sale" button to clear current_sale
# Figure out how to track idividual sales and organize into days


class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.items = []
            self.prices = []
            today = str(datetime.today())
            self.current_sale = {"sale_date": today}

            # Labels for entry fields
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_item = tk.Label(self, text="Item: ")
            l_price = tk.Label(self, text="Price: ")
            l_sales.grid(row=0, column=0)
            l_item.grid(row=2, column=0)
            l_price.grid(row=3, column=0)

            # Entry fields for item & price
            self.e_item = tk.Entry(self, text="item1")
            self.e_item.grid(row=2, column=1)
            self.e_price = tk.Entry(self, text="price1")
            self.e_price.grid(row=3, column=1)

            # Buttons for page functions
            b_add_to_sale = tk.Button(self, text="Add to Sale", command=lambda: [get_entries()])
            b_get_total = tk.Button(self, text="Get Total", command=lambda: get_total())
            b_add_to_ledger = tk.Button(self, text="Add to Sales Ledger", command=lambda: add_to_cs())
            b_add_to_sale.grid(row=10, column=0)
            b_get_total.grid(row=11, column=0)
            b_add_to_ledger.grid(row=12, column=0)

            # Buttons for page selection
            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.SalesLedger))
            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_home_page.grid(row=20, column=11)
            b_ledger.grid(row=20, column=12)            
            b_products_page.grid(row=20, column=13)
            b_totals_page.grid(row=20, column=14)

            # Quit button
            b_quit = tk.Button(self, text="Close", command=self.quit)
            b_quit.grid(row=30, column=0)

            def get_entries():
                # Dumps entries to json file to be used by current_sale
                # Need to fix: updates current_sale with multiples of last item
                item = self.e_item.get()
                price = self.e_price.get()
                self.items.append(item)
                self.prices.append(price)
                print(f"Added items: {item}, ${price}")
                self.e_item.delete(0, tk.END)
                self.e_price.delete(0, tk.END)

            def get_total():
                nums = self.prices
                subtotal = 0
                for num in nums:
                    subtotal = subtotal + float(num)
                total = subtotal * 1.13
                total = round(total, 2)
                print(f"Subtotal: ${subtotal}\nTotal: ${total}")
                return subtotal, total

            def add_to_cs():
                for i in range(0, len(self.items)):
                    k = "item_" + str(i)
                    self.current_sale.update({k: [self.items[i], self.prices[i]]})
                print(self.current_sale)

