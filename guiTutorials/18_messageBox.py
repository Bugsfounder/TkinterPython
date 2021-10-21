from tkinter import *
import tkinter.messagebox as tmsg

def myFunc():
    print("Mai ek Bahut hi Natkhat aur Shaitan Function hun☻☺!♥U")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "Harry will Help you with this gui")

def rate():
    print("Rate Us")
    value = tmsg.askquestion("Was Your Experience Good?", "You used this GUI... was Your Experience Good?")
    if value=="yes":
        msg = "Great Please Rate us on AppStore Please"
    else:
        msg = "Tell us What will wrong We will call You soon"

    tmsg.showinfo("Experience", msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti kar lo", "Sorry Divya nahi banegi apki dost")
    if ans:
        print("Retry karne pe bhi kuchh nahi hoga")
    else:
        print("Bahut Badhiya bhai cancel kar dia barna pitte")


def first():
    ans = tmsg.askyesnocancel("Are Your First", "Are You First Or Not")
    print(ans)
    if ans:
        tmsg.showinfo("Congrates", "Congrates your are the first person who is using this superb gui")
    elif ans == False:
        tmsg.showwarning("Not First", "You are not first person who used this gui")
    else:
        tmsg.showerror("Cancle", "Please Don't Cancel this choose yes or no")

# GUI STARTS HERE
root = Tk()
root.title("Menues and Submenues in Python Using Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH


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


m3 = Menu(mainMenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="first", command=first)
m3.add_command(label="BeFriend Divya", command=divya)
mainMenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainMenu)


# GUI ENDS HERE
root.mainloop()