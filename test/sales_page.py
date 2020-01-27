from datetime import datetime
import tkinter as tk
from tkinter import messagebox as mb
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
# Fix  make_csv() - add to "New Sale" button once finished
# Figure out how to track idividual sales and organize into days

# Set names for files that will be created
# CSV will contain datetime, sale total, and pay type
# JSON will contain datetime, sale total, pay type, and items
ledger_csv = 'ledger.csv'
ledger_json = 'ledger.json'

class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.items = []
            self.prices = []
            self.pay_type = []
            today = str(datetime.today())
            # current_sale will be a dictionary containing the sale info until cleared
            # It contains the current date, and will be appended with total, subtotal, and items from the sale
            self.current_sale = {"date": today}

            # Labels for entry fields
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_item = tk.Label(self, text="Item: ")
            l_price = tk.Label(self, text="Price: ")
            l_pay_type = tk.Label(self, text="Pay Type: ")
            l_sales.grid(row=0, column=0)
            l_item.grid(row=2, column=0)
            l_price.grid(row=3, column=0)
            l_pay_type.grid(row=4, column=0)

            # Entry fields for item & price
            self.e_item = tk.Entry(self, text="item1")
            self.e_price = tk.Entry(self, text="price1")
            self.e_pay_type = tk.Entry(self, text="pay_type")
            self.e_item.grid(row=2, column=1)
            self.e_price.grid(row=3, column=1)
            self.e_pay_type.grid(row=4, column=1)
            

            # Buttons for page functions
            b_add_to_sale = tk.Button(self, text="Add to Sale", command=lambda: get_entries())
            b_get_total = tk.Button(self, text="Get Total", command=lambda: get_total())
            b_add_to_ledger = tk.Button(self, text="Append Sale", command=lambda: add_to_cs())
            b_new_sale = tk.Button(self, text="New Sale", command=lambda: new_sale(ledger_csv))
            b_clear_sale = tk.Button(self, text="Clear Sale", command=lambda: clear_sale())
            b_show_sale = tk.Button(self, text="Show Sale", command=lambda: show_sale())
            b_add_to_sale.grid(row=10, column=0)
            b_get_total.grid(row=11, column=0)
            b_add_to_ledger.grid(row=12, column=0)
            b_new_sale.grid(row=13, column=1)
            b_clear_sale.grid(row=13, column=0)
            b_show_sale.grid(row=14, column=0)

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
                # Gets entries from item and price fields, appends to list if int/float
                item = self.e_item.get()
                price = self.e_price.get()
                try:
                    price = float(price)
                    self.items.append(item)
                    self.prices.append(price)
                    print(f"Added items: {item}, ${price}")
                except ValueError:
                    print("Please only enter numbers in the \"Price\" field.")
                self.e_item.delete(0, tk.END)
                self.e_price.delete(0, tk.END)

            def get_total():
                # Returns subtotal and total after tax
                nums = self.prices
                subtotal = 0
                tax = 1.13
                for num in nums:
                    subtotal = subtotal + float(num)
                subtotal = round(subtotal, 2)
                total = subtotal * tax
                total = round(total, 2)
                print(f"Subtotal: ${subtotal}\nTotal: ${total}")
                return total, subtotal

            def add_to_cs():
                # Adds items from items and prices to current_sale dictionary
                nums = get_total()
                subtotal = nums[0]
                total = nums[1]
                self.current_sale.update({"subtotal": subtotal})
                self.current_sale.update({"total": total})
                for i in range(0, len(self.items)):
                    k = "item_" + str(i)
                    self.current_sale.update({k: [self.items[i], self.prices[i]]})
                print(self.current_sale)

            def make_csv(csv_fp):
                ### NEED TO FIX
                data_layout = [datetime.now(), self.current_sale["total"]]
                df = pd.DataFrame(data_layout, columns = ['Total', 'Pay Type', 'Date'])
                if os.path.isfile(csv_fp):
                    csv = df.to_csv(csv_fp, mode='a', header=False)
                else:
                    csv = df.to_csv(csv_fp, mode='a', header=True)

            def clear_sale():
                # Clears items, prices, and current_sale to begin new one
                self.items = []
                self.prices = []
                self.current_sale = {"sale_date": today}
                self.e_item.delete(0, tk.END)
                self.e_price.delete(0, tk.END)
                self.e_pay_type.delete(0, tk.END)
                print("Sale cleared. Begin new sale.")

            def new_sale(csv_fp):
                # Checks to make sure pay_type added to sale, then adds pay_type to current_sale, 
                # adds any enterd items to sale, and clears current_sale to begin new one
                # 
                if self.e_pay_type.get() == "":
                    print("Please enter pay type.")
                else:
                    pay_type = self.e_pay_type.get()
                    self.current_sale({"pay_type": pay_type})
                    add_to_cs()
                    #make_csv(csv_fp)
                    print(f"Sale completed: {self.current_sale}")
                    clear_sale()

            def show_sale():
                date = self.current_sale["date"]
                subtotal = self.current_sale["subtotal"]
                total = self.current_sale["total"]
                structure = f"Date: {date}, Subtotal: {subtotal}, Total: {total}"
                mb.showinfo("Current Sale", structure)