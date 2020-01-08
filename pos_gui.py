from tkinter import *

class POS(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("POS")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # File menu
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        # Edit menu
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        # Pages menu
        pages = Menu(menu)
        pages.add_command(label="Home")
        pages.add_command(label="Sales Ledger")
        pages.add_command(label="Inventory")
        pages.add_command(label="Totals")
        menu.add_cascade(label="Pages", menu=pages)

        exit_button = Button(self, text="Exit", command=self.client_exit)
        exit_button.place(x=0, y=0)

    def client_exit(self):
        exit()

root = Tk()

root.geometry("1200x700")
app = POS(root)

root.mainloop()