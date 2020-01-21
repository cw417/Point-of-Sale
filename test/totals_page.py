import tkinter as tk
import home_page as hp 
import sales_page as sp
import ledger_page as lp 
import products_page as pp 
import page_settings

LARGE_FONT = ("Verdana", 12)

class Totals(tk.Frame):


        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_totals = tk.Label(self, text="Totals", font=page_settings.LARGE_FONT)
            l_totals.grid(row=0, column=0)

            b_home_page = tk.Button(self, text="Home Page", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=1, column=0)
                        
            b_sales_page = tk.Button(self, text="Sales", command=lambda: controller.show_frame(sp.Sales))
            b_sales_page.grid(row=2, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.Ledger))
            b_ledger.grid(row=3, column=0)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=4, column=0)

            b_close = tk.Button(self, text="Close", command=self.quit)
            b_close.grid(row=30, column=0)