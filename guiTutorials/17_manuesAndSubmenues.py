from tkinter import *

def myFunc():
    print("Mai ek Bahut hi Natkhat aur Shaitan Function hun☻☺!♥U")

# GUI STARTS HERE
root = Tk()
root.title("Menues and Submenues in Python Using Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

# USE THESE TO CREATE A NON DROP DOWN MENU
# myMenue  = Menu(root)
# myMenue.add_command(label="File", command=myFunc)
# myMenue.add_command(label="Exit", command=quit)
# root.config(menu=myMenue)

mainMenu = Menu(root)
# m1 = Menu(mainMenu)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="New Project", command=myFunc)
m1.add_command(label="Save", command=myFunc)
m1.add_separator()
m1.add_command(label="Save As", command=myFunc)
m1.add_command(label="Print", command=myFunc)
mainMenu.add_cascade(label="File", menu=m1)
root.config(menu=mainMenu)

m2 = Menu(mainMenu)
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Copy", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
m2.add_command(label="Find", command=myFunc)
m2.add_separator()
m2.add_command(label="Exit", command=quit)
mainMenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainMenu)
# GUI ENDS HERE
root.mainloop()