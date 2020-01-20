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

def get_total(current_sale_fp):
    sale = get_dict(current_sale_fp)
    vals = sale.values()
    sale_nums = check_nums(vals)
    print(f"Sale nums: {sale_nums}")
    subtotal = add_total(sale_nums)
    total = subtotal * 1.13
    print(subtotal, total)
    return subtotal, total


# Will have sale value and current_sale value
# current_sale will be written and appended with "Add to Sale" button
# current_sale will be appended to ledgerand cleared once "Checkout" button is pressed
# current_sale will be displayed to the right of the entry fields
# Checkout button: add current_sale to sales ledger and delete current_sale file
# Buttons: add_to_sale, checkout

#TO DO: 
# Make Total button to display totals, clear current_sale, and add sale to ledger.json
# Find way to display sale as entered
# 


class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_sales.grid(row=0, column=0)

            l_item1 = tk.Label(self, text="Item: ")
            l_item1.grid(row=2, column=0)
            l_price1 = tk.Label(self, text="Price: ")
            l_price1.grid(row=3, column=0)
            l_item2 = tk.Label(self, text="Item: ")
            l_item2.grid(row=4, column=0)
            l_price2 = tk.Label(self, text="Price: ")
            l_price2.grid(row=5, column=0)
            l_item3 = tk.Label(self, text="Item: ")
            l_item3.grid(row=6, column=0)
            l_price3 = tk.Label(self, text="Price: ")
            l_price3.grid(row=7, column=0)
            l_item4 = tk.Label(self, text="Item: ")
            l_item4.grid(row=8, column=0)
            l_price4 = tk.Label(self, text="Price: ")
            l_price4.grid(row=9, column=0)


            e_item1 = tk.Entry(self, text="item1")
            e_item1.grid(row=2, column=1)
            e_price1 = tk.Entry(self, text="price1")
            e_price1.grid(row=3, column=1)
            e_item2 = tk.Entry(self, text="item2")
            e_item2.grid(row=4, column=1)
            e_price2 = tk.Entry(self, text="price2")
            e_price2.grid(row=5, column=1)
            e_item3 = tk.Entry(self, text="item3")
            e_item3.grid(row=6, column=1)
            e_price3 = tk.Entry(self, text="price3")
            e_price3.grid(row=7, column=1)
            e_item4 = tk.Entry(self, text="item4")
            e_item4.grid(row=8, column=1)
            e_price4 = tk.Entry(self, text="price4")
            e_price4.grid(row=9, column=1)
            
            def get_entries():
                dict = {}

                item1 = e_item1.get()
                dict.update({"item1": item1})
                price1 = e_price1.get()
                dict.update({"price1": price1})
                item2 = e_item2.get()
                dict.update({"item2": item2})
                price2 = e_price2.get()
                dict.update({"price2": price2})
                item3 = e_item3.get()
                dict.update({"item3": item3})
                price3 = e_price3.get()
                dict.update({"price3": price3})
                item4 = e_item4.get()
                dict.update({"item4": item4})
                price4 = e_price4.get()
                dict.update({"price4": price4})

                if not os.path.isfile(current_sale_fp):
                    json.dump(dict, open(current_sale_fp, 'w'), indent=4, sort_keys=True)
                else:
                    json.dump(dict, open(current_sale_fp, 'a'), indent=4, sort_keys=True)


            b_add_to_sale = tk.Button(self, text="Add to Sale", command=get_entries)
            b_add_to_sale.grid(row=10, column=0)

            b_get_total = tk.Button(self, text="Get Total", command=lambda: get_total(current_sale_fp))
            b_get_total.grid(row=11, column=0)

            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=20, column=11)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.SalesLedger))
            b_ledger.grid(row=20, column=12)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=20, column=13)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=20, column=14)
