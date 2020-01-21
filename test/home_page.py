import tkinter as tk
import sales_page as sp
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings


class HomePage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_home = tk.Label(self, text="Home Page", font=page_settings.LARGE_FONT)
            l_home.grid(row=0, column=0)

            b_sales_page = tk.Button(self, text="Sales", command=lambda: controller.show_frame(sp.Sales))
            b_sales_page.grid(row=10, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.Ledger))
            b_ledger.grid(row=10, column=1)

            b_products_page = tk.Button(self, text="Products", command=lambda: controller.show_frame(pp.Products))
            b_products_page.grid(row=10, column=2)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=10, column=3)

            b_close = tk.Button(self, text="Close", command=self.quit)
            b_close.grid(row=30, column=0)
