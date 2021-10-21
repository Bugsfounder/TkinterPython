from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i = 0
# GUI STARTS HERE
root = Tk()
root.title("ListBox in Python Using Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Item of Out List Box")

Button(root, text='Add Item', command=add).pack()

# GUI ENDS HERE
root.mainloop()