

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        self.entry =  Entry(master, width=20, bg="dark grey")
        self.entry.grid(row = 2, column = 0, columnspan = 6, sticky = W)
        self.entry.focus_set()




root = Tk()
root.geometry()
root.title("Stats Done The Right Way")
app = Application (root)
root.mainloop()