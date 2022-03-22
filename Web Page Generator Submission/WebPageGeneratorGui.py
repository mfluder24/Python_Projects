import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import ttk

# Frame is the parent class in tkinter
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 170))
        self.master.title('Update Web Page')
        self.master.config(bg='lightgray')

        self.txtText = Text(self.master, height=5, width=60)
        self.txtText.grid(row=0, column=0, padx=7, pady=5)

        self.btnCheck = Button(self.master, text="Update Page", width=15, height=3, command=self.submit)
        self.btnCheck.grid(row=2, column=0, padx=(15,0), pady=(10,0), sticky= NW)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3, command= self.cancel)
        self.btnClose.grid(row=2, column=0, padx=(0,15), pady=(10,0), sticky= E)

# Function that gets user input from Text and concatenates it into basic HTML code
    def submit(self):
        bodytxt = self.txtText.get("1.0","end-1c")
        url = 'sale.html'
        # Creating html file
        Func = open("sale.html","w")
        Func.write("<html>\n<body>\n<h1> \n"+ bodytxt +" \
            </h1>\n</body>\n</html>")
        Func.close()
        # Opening html file in new tab
        webbrowser.open_new_tab(url)
        # Printing user input to IDLE just as another place to see it :)
        print(bodytxt)


    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

