import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

# Importing other modules to have access to them
import phonebook_main
import phonebook_gui



def center_window(self, w, h): # Pass in Tkinter frame (Master) reference, and w & h
    # Get user's screen width & height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate X & Y coordinates to center the app on user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Catch if user clicks on upper-right 'X' in window to ensure they want to close window
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        # This closes the application
        self.master.destroy()
        os._exit(0)


#======================================================

def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_Fname TEXT, \
            col_Lname TEXT, \
            col_Fullname TEXT, \
            col_Phone TEXT, \
            col_Email TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('Brock','Rumlow','Brock Rumlow','555-555-5555','brumlow@strike.com')
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_Fname, col_Lname, col_Fullname, col_Phone, col_Email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','555-555-5555','jdoe@email.com'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count


# Select an item in ListBox
def onSelect(self,event):
    # Calling event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_Fname, col_Lname, col_Phone, col_Email FROM tbl_phonebook WHERE col_Fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple, which can be sliced into 4 parts using data[] during iteration
        for data in varBody:
            self.txt_Fname.delete(0,END)
            self.txt_Fname.insert(0,data[0])
            self.txt_Lname.delete(0,END)
            self.txt_Lname.insert(0,data[1])
            self.txt_Phone.delete(0,END)
            self.txt_Phone.insert(0,data[2])
            self.txt_Email.delete(0,END)
            self.txt_Email.insert(0,data[3])


def addToList(self):
    var_Fname = self.txt_Fname.get()
    var_Lname = self.txt_Lname.get()
    # Normalise data to keep it consistent in the dB
    var_Fname = var_Fname.strip() # Removes any blank spaces before & after user's entry
    var_Lname = var_Lname.strip()
    var_Fname = var_Fname.title() # Ensures that first char in each word is capitalised
    var_Lname = var_Lname.title()
    var_Fullname = ("{} {}".format(var_Fname,var_Lname)) # Combines normalised values into a proper full name
    print("var_Fullname: {}".format(var_Fullname))
    var_Phone = self.txt_Phone.get().strip()
    var_Email = self.txt_Email.get().strip()
    if not "@" or not "." in var_Email:
        print("Incorrect email format.")
    # Enforce user to provide required information    
    if (len(var_Fname) > 0) and (len(var_Lname) > 0) and (len(var_Phone) > 0) and (len(var_Email) > 0):
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the dB for existance of full name, if found will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_Fullname) FROM tbl_phonebook WHERE col_Fullname = '{}'""".format(var_Fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # If == 0, there is no prior existance of fullname and new data can be added
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_Fname, col_Lname, col_Fullname, col_Phone, col_Email) VALUES (?,?,?,?,?)""",(var_Fname,var_Lname,var_Fullname,var_Phone,var_Email))
                self.lstList1.insert(END, var_Fullname) # Update ListBox with the new fullname
                onClear(self) # Call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_Fullname))
                onClear(self) # Call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that all fields have been filled out.")


def onDelete(self):
    var_Select = self.lstList1.get(self.lstList1.curselection()) # ListBox's selected value
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # Check count to ensure this is not last record in the dB
        # as last record cannot be deleted or there will be an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with ({}) \nwill be permenantly deleted from the database. \n\nProceed with deletion?".format(var_Select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_Select))
                onDeleted(self) # Call the function to clear all of the textboxes & selected index of listbox
##                onRefresh(self) # Update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before deleting ({}).".format(var_Select,var_Select))
    conn.close()


def onDeleted(self):
    # Clear the text in the specified textboxes
    self.txt_Fname.delete(0,END)
    self.txt_Lname.delete(0,END)
    self.txt_Phone.delete(0,END)
    self.txt_Email.delete(0,END)
##    onRefresh(self)  # Update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    # Clear the text in the specified textboxes
    self.txt_Fname.delete(0,END)
    self.txt_Lname.delete(0,END)
    self.txt_Phone.delete(0,END)
    self.txt_Email.delete(0,END)



def onRefresh(self):
    # Populate the listbox coinciding with the dB
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_Fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_Select = self.lstList1.curselection()[0] # Index of the list selection
        var_Value = self.lstList1.get(var_Select) # List selection's text value
    except:
        messagebox.showinfo("Missing Selection","No name was selected from the list box. \nCancelling the Update Request.")
        return
    # The user will only be allowed to update changes for phone and emails.
    # For name changes, the user will beed to delete the entire record and start over.
    var_Phone = self.txt_Phone.get().strip() # Normalise the data to maintain db integrity
    var_Email = self.txt_Email.get().strip()
    if (len(var_Phone) > 0) and (len(var_Email) > 0): # Ensure there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # Count records to see if the user's changes are already in
            # the dB, meaning there are no changes to update.
            cur.execute("""SELECT COUNT(col_Phone) FROM tbl_phonebook WHERE col_Phone = '{}'""".format(var_Phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_Email) FROM tbl_phonebook WHERE col_Email = '{}'""".format(var_Email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # If Proposed changes are not already in the dB, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the Update Request?".format(var_Phone,var_Email,var_Value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_Phone = '{0}',col_Email = '{1}' WHERE col_Fullname = '{2}'""".format(var_Phone,var_Email,var_Value))
                        onClear(self)
                        conn.commit()
                else:
                    message.showinfo("Cancel request","No changes have been made to ({}).".format(var_Value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_Phone,var_Email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing iformation","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)                


if __name__ == "__main__":
    pass
