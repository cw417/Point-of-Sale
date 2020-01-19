from datetime import datetime
import tkinter as tk
import home_page as hp 
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings
import json
import os


ledger_json = 'ledger.json'
stock_json = 'stock.json'
current_sale_fp = 'current_sale.json'
current_sale = {}

def sale_to_ledger(sale):
    json.dump(sale, open(ledger_fp, 'a'), indent=4, sort_keys=True)

def get_dict(json_fp):
    with open(json_fp) as json_data:
        dict = json.load(json_data)
        json_data.close()
        return dict

def search_stock(item):
    # Needs to be configured for 'stock.json'
    # Need to figure out format for stock dictionary entries
    stock = get_dict(stock_json)
    for stock_item in stock:
        if item["name"] == stock_item:
            name = stock_item["name"]
            price = stock_item["price"]
            current_sale[name] = price
            # Need to write parameters for creating and adding to a current sale


def check_nums(nums):
    # Checks to see if items in list are digits, and returns list of items that are
    num_list = []
    for num in nums:
        if isinstance(num, int) == True or isinstance(num, float):
            num = float(num)
            num_list.append(num)
    return num_list

def add_total(total_list):
    # Adds up items in a list, and returns the total
    total = 0
    for num in total_list:
        total += num
    return total

def add_to_sale(item, price):
    current_sale[item] = price

def get_total(sale):
    vals = sale.values()
    sale_nums = check_nums(vals)
    subtotal = add_total(sale_nums)
    total = subtotal * 1.13
    return subtotal, total


# Will have sale value and current_sale value
# current_sale will be written and appended with "Add to Sale" button
# current_sale will be appended to ledgerand cleared once "Checkout" button is pressed
# current_sale will be displayed to the right of the entry fields
# Checkout button: add current_sale to sales ledger and delete current_sale file
# Buttons: add_to_sale, checkout


class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_sales.grid(row=0, column=0)

            l_item = tk.Label(self, text="Enter item: ")
            l_item.grid(row=2, column=0)
            l_price = tk.Label(self, text="Enter price: ")
            l_price.grid(row=3, column=0)

            e_item = tk.Entry(self, text="Enter item: ")
            e_item.grid(row=2, column=1)
            e_price = tk.Entry(self, text="Enter price: ")
            e_price.grid(row=3, column=1)

            
            def get_entries():
                dict = {}

                item = e_item.get()
                dict.update({"item": item})
                price = e_price.get()
                dict.update({"price": price})

                if not os.path.isfile(current_sale_fp):
                    json.dump(dict, open(current_sale_fp, 'w'), indent=4, sort_keys=True)
                else:
                    json.dump(dict, open(current_sale_fp, 'a'), indent=4, sort_keys=True)


            b_add_to_sale = tk.Button(self, text="Add to Sale", command=get_entries)
            b_add_to_sale.grid(row=4, column=0)

            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=10, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.SalesLedger))
            b_ledger.grid(row=10, column=1)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=10, column=2)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=10, column=3)
