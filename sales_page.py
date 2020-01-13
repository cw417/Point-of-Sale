import tkinter as tk
import home_page as hp 
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings
import json
import datetime as date


def get_dict(json_fp):
    with open(json_fp) as json_data:
        pyscrape_dict = json.load(json_data)
        json_data.close()
        return pyscrape_dict

def search_stock(item):
    stock = 
    for stock_item in stock:
        if item == stock_item:
            stock_item.get()
            # Need to write parameters for creating and adding to a current sale

def isdigit_list(nums):
    # Checks to see if items in list are digits, and returns list of items that are
    num_list = []
    for num in nums:
        if num.isdigit() == True:
            num = int(num)
            num_list.append(num)
    return num_list
    

def get_total(total_list):
    # Adds up items in a list, and returns the total
    total = 0
    for num in total_list:
        total += num
    return total
        
def create_sale():
    # Used to create sale from items in current sale
    # Need to add iterative function to add multitple items
    sale = {}
    sale_keys = sale.keys()
    sale_digits = isdigit_list(sale_keys)
    subtotal = get_total(sale_digits)
    total = subtotal * 1.13

    sale["date"] = date.today()
    sale["item"] = "price"
    sale["subtotal"] = subtotal
    sale["total"] = total

    return sale

def sale_to_json(sale)
    json.dump(sale, open('sales_dict.json', 'a'), indent=4, sort_keys=True)
    json.dump(sale, open('current_sale.json', 'w'), indent=4, sort_keys=True)

class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_sales.grid(row=0, column=0)

            e_search_item = tk.Entry(self, text="Type item to search: ")
            e_search_item.grid(row=1, column=0)

            b_search_item = tk.Button(self, text="Search", command=search_stock)
            b_search_item.grid(row=2, column=0) 

            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=3, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.SalesLedger))
            b_ledger.grid(row=3, column=1)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=3, column=2)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=3, column=3)
