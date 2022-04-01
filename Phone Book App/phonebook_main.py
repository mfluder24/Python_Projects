# Python:     Ver 3.5.1
#
# Author:     Fox Addams
#
# Purpose:    Phonebook demo. Demonstrating Object-Oriented Programming (OOP),
#             Tkinter GUI module, & using Tkinter Parent & Child relationships.
#
# Tested OS:  This code was written and tested with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Importing other modules to have access to them
import phonebook_gui
import phonebook_func

# Frame = Tkinter frame class our own class inherits from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defining Master frame config
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # CenterWindow method centers app on user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # Protocol method is a Tkinter built-in method to catch if
        # the user clicks the upper right corner, 'X' on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in GUI widgets from a separate module,
        # keeping code compartmentalised and clutter free
        phonebook_gui.load_gui(self)








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
