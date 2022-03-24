# Python:     Ver 3.10.2
#
# Author:     Fox Addams
#
# Purpose:    File transfer demo. Demonstrating Object-Oriented Programming (OOP),
#             Tkinter GUI module, shutil, os and datetime.
#
# Tested OS:  This code was written and tested with Windows 10.

import shutil
import os
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

gui = Tk()
gui.geometry("450x180")
gui.title("File Transfer")

# Gui and folder select
class FolderSelect(Frame):
    def __init__(self,parent=None,folderDesc="",**kw):
        Frame.__init__(self,master=parent,**kw)
        
        self.folderPath = StringVar()
        
        self.lblName = Label(self, text=folderDesc)
        self.lblName.grid(row=0,column=0, padx=(10,0), pady=(10,0), sticky=N+W)
        
        self.txtPath = Entry(self, textvariable=self.folderPath)
        self.txtPath.grid(row=1,column=0, padx=(15,0), ipadx=100)
        
        self.btnFind = ttk.Button(self, text="Browse...",command=self.setFolderPath)
        self.btnFind.grid(row=1,column=2, padx=(15,0))
        
    def setFolderPath(self):
        folderSelected = filedialog.askdirectory()
        self.folderPath.set(folderSelected)
        
    @property
    def folder_path(self):
        return self.folderPath.get()


# Get list of files that match desired path
def FileList(path):
    return [os.path.join(path, file) for file in os.listdir(path)]

def copyFiles():
    source = srcFolder.folder_path
    
    # Create list of file names from source folder
    files = FileList(source)
    
    for i in files:
        # Find date last modified and current date
        modDate = datetime.datetime.fromtimestamp(os.path.getmtime(i))
        currentDate = datetime.datetime.today()
        # Create list from file path
        pathList = i.split("\\")
        
        # Only get file name element from list
        file = pathList[1]
        
        # Makes variable greater than current date if updated within last 24 hours
        recentMod = modDate + datetime.timedelta(days=1)

        # Completes file path so file is copied to proper location
        dest = destFolder.folder_path + "/" + file
        
        # Compares variables, copies recently modded to destination folder
        if recentMod > currentDate:
            shutil.copy2(i, dest)
            print("File copied!", file)

folderPath = StringVar()

srcFolder = FolderSelect(gui,"Source Folder:")
srcFolder.grid(row=0)

destFolder = FolderSelect(gui,"Destination Folder:")
destFolder.grid(row=1)

c = ttk.Button(gui, text="Copy Files", command=copyFiles)
c.grid(row=4,column=0, pady=(15,0))
gui.mainloop()
