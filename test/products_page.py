import tkinter as tk
import home_page as hp 
import sales_page as sp
import ledger_page as lp
import totals_page as tp
import page_settings


class Products(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            l_products = tk.Label(self, text="Products", font=page_settings.LARGE_FONT)
            l_products.grid(row=0, column=0)

            b_home_page = tk.Button(self, text="Home", command=lambda: controller.show_frame(hp.HomePage))
            b_home_page.grid(row=1, column=0)
            
            b_sales_page = tk.Button(self, text="Sales", command=lambda: controller.show_frame(sp.Sales))
            b_sales_page.grid(row=2, column=0)

            b_ledger = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(lp.Ledger))
            b_ledger.grid(row=3, column=0)

            b_totals_page = tk.Button(self, text="Totals", command=lambda: controller.show_frame(tp.Totals))
            b_totals_page.grid(row=4, column=0)

            b_close = tk.Button(self, text="Close", command=self.quit)
            b_close.grid(row=30, column=0)
