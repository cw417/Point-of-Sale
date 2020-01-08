from tkinter import *

class POS(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("POS")
        self.pack(fill=BOTH, expand=1)

        close_button = Button(self, text="Close", command=self.client_close)

        close_button.place(x=0, y=0)

    def client_close(self):
        exit()

root = Tk()

root.geometry("1200x700")
app = POS(root)

root.mainloop()