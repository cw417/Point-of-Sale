import tkinter as tk
import home_page as hp 
import sales_page as sp
import products_page as pp 
import totals_page as tp
import page_settings


class Ledger(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_ledger = tk.Label(self, text="Sales Ledger", font=page_settings.LARGE_FONT)
            l_ledger.grid(row=0, column=0)

            # Buttons for other pages
            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_sales_page = tk.Button(self, text="Sales", command=lambda: controller.show_frame(sp.Sales))
            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_home_page.grid(row=1, column=0)
            b_sales_page.grid(row=2, column=0)
            b_products_page.grid(row=3, column=0)
            b_totals_page.grid(row=4, column=0)

            # Close button
            b_close = tk.Button(self, text="Close", command=self.quit)
            b_close.grid(row=30, column=0)

            def nest_dict_iter(sale_dict):
                # Iterates through nested dictionaries to return nested values
                for k, v in sale_dict.items():
                    for i in range(0,1):
                        name = "item_" + str(i)
                        if name in k:
                            for t, c in v.items():
                                print(c)
            
            #def dict_list_iter(sale_dict):