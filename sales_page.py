import tkinter as tk
import home_page as hp 
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings


class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_sales = tk.Label(self, text="Sales", font=page_settings.LARGE_FONT)
            l_sales.grid(row=0, column=0)

            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=1, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.Ledger))
            b_ledger.grid(row=2, column=0)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=3, column=0)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=4, column=0)
