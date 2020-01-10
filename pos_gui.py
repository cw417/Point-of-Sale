import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class POS(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Sales, SalesLedger, Products, Totals):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[F] = frame
        
        frame.grid(row=0, column=0, stick="nsew")
        
        self.show_frame(HomePage)
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            home_label = tk.Label(self, text="Home Page", font=LARGE_FONT)
            home_label.grid(row=0, column=0)

            sales_button = tk.Button(self, text="Sales", command=lambda: controller.show_frame(Sales))
            sales_button.grid(row=1, column=0)

            ledger_button = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(SalesLedger))
            ledger_button.grid(row=2, column=0)

            products_button = tk.Button(self, text="Products", command=lambda: controller.show_frame(Products))
            products_button.grid(row=3, column=0)

            totals_button = tk.Button(self, text="Totals", command=lambda: controller.show_frame(Totals))
            totals_button.grid(row=4, column=0)

class Sales(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            sales_label = tk.Label(self, text="Sales", font=LARGE_FONT)
            sales_label.grid(row=0, column=0)

            home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
            home_button.grid(row=1, column=0)

            ledger_button = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(SalesLedger))
            ledger_button.grid(row=2, column=0)

            products_button = tk.Button(self, text="Products", command=lambda: controller.show_frame(Products))
            products_button.grid(row=3, column=0)

            totals_button = tk.Button(self, text="Totals", command=lambda: controller.show_frame(Totals))
            totals_button.grid(row=4, column=0)

class SalesLedger(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Sales Ledger", font=LARGE_FONT)
            label.grid(row=0, column=0)

            home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
            home_button.grid(row=1, column=0)

            sales_button = tk.Button(self, text="Sales", command=lambda: controller.show_frame(Sales))
            sales_button.grid(row=2, column=0)

            products_button = tk.Button(self, text="Products", command=lambda: controller.show_frame(Products))
            products_button.grid(row=3, column=0)

            totals_button = tk.Button(self, text="Totals", command=lambda: controller.show_frame(Totals))
            totals_button.grid(row=4, column=0)

class Products(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Products", font=LARGE_FONT)
            label.grid(row=0, column=0)

            home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
            home_button.grid(row=1, column=0)
            
            sales_button = tk.Button(self, text="Sales", command=lambda: controller.show_frame(Sales))
            sales_button.grid(row=2, column=0)

            ledger_button = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(SalesLedger))
            ledger_button.grid(row=3, column=0)

            totals_button = tk.Button(self, text="Totals", command=lambda: controller.show_frame(Totals))
            totals_button.grid(row=4, column=0)

class Totals(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Totals", font=LARGE_FONT)
            label.grid(row=0, column=0)

            button = tk.Button(self, text="Home Page", command=lambda: controller.show_frame(HomePage))
            button.grid(row=1, column=0)
                        
            sales_button = tk.Button(self, text="Sales", command=lambda: controller.show_frame(Sales))
            sales_button.grid(row=2, column=0)

            ledger_button = tk.Button(self, text="Sales Ledger", command=lambda: controller.show_frame(SalesLedger))
            ledger_button.grid(row=3, column=0)

            products_button = tk.Button(self, text="Products", command=lambda: controller.show_frame(Products))
            products_button.grid(row=4, column=0)


app = POS()

app.geometry("1200x700")

app.mainloop()

