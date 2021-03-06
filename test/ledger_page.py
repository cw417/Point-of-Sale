import tkinter as tk
import home_page as hp 
import sales_page as sp
import products_page as pp 
import totals_page as tp
import page_settings
import json


class Ledger(tk.Frame):

        def __init__(self, parent, controller):
            # Intialize frame and variables
            tk.Frame.__init__(self, parent)
            self.ledger_json = 'ledger.json'
            self.ledger_dict = {}

            # Main page label
            l_ledger = tk.Label(self, text="Sales Ledger", font=page_settings.LARGE_FONT)
            l_ledger.grid(row=0, column=0)

            # Page labels
            l_search_date = tk.Label(self, text="Enter date to search\n (YYYY-MM-DD):")
            l_search_date.grid(row=2, column=0)

            # Entry fields
            e_search_date = tk.Entry(self, text="date_search")
            e_search_date.grid(row=2, column=1)

            # Page-specific buttons
            b_load_ledger = tk.Button(self, text="Load Ledger", command=lambda: [load_dict(self.ledger_json), e_search_date.focus()])
            b_search_date = tk.Button(self, text="Search")
            b_load_ledger.grid(row=1, column=0)
            b_search_date.grid(row=3, column=0)

            # Page navigation buttons
            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_sales_page = tk.Button(self, text="Sales", command=lambda: controller.show_frame(sp.Sales))
            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_home_page.grid(row=30, column=10)
            b_sales_page.grid(row=30, column=11)
            b_products_page.grid(row=30, column=12)
            b_totals_page.grid(row=30, column=13)

            # Close button
            b_close = tk.Button(self, text="Close", command=self.quit)
            b_close.grid(row=31, column=0)

            def load_dict(json_fp):
                # Loads ledger json from given fp and assigns to self.ledger_dict
                try:
                    with open(json_fp, 'r') as fp:
                        ledger_dict = json.load(fp)
                        self.ledger_dict = ledger_dict
                        print(self.ledger_dict)
                except FileNotFoundError:
                    print("Sorry, but the ledger file could not be found in the current directory.")

            def nest_iter_0(sale_dict):
                # NOT FUNCTIONAL
                # Iterates through nested dictionaries to return nested values
                # TODO: Needs to look for specified key and return value
                # TODO: Need to reformat how sales_page saves sale to json
                for k, v in sale_dict.items():
                    for i in range(0,1):
                        name = "item_" + str(i)
                        if name in k:
                            for t, c in v.items():
                                c = f"{t}: {c}"
                                print(c)

            def nest_iter_1(sale_dict):
                # Iterates through nested dictionaries to return nested values
                # TODO: Needs to look for specified key and return value
                for k, v in sale_dict.items():
                    for i in range(0,len(sale_dict.items())):
                        name = "item_" + str(i)
                        if name in k:
                            try:
                                for t, c in v.items():
                                    c = f"{t}: {c}"
                                    print(c)
                            except AttributeError:
                                print(f"{k}: {v}")
            