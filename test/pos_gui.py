import tkinter as tk
import home_page as hp 
import sales_page as sp
import ledger_page as lp 
import products_page as pp 
import totals_page as tp
import page_settings

class POS(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (hp.HomePage, sp.Sales, lp.Ledger, pp.Products, tp.Totals):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[F] = frame
        
        frame.grid(row=0, column=0, stick="nsew")
        
        self.show_frame(hp.HomePage)
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

app = POS()

app.geometry("800x400")

app.mainloop()