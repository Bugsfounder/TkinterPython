from tkinter import *

def getVals():
    print(f"The Value of username is: {userValue.get()} and the value of password is: {passwordValue.get()}")

root = Tk()

root.geometry('500x400')

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, IntVar, StringVar, DoubleVar
userValue = StringVar()
passwordValue = StringVar()

userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passwordValue)

userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

Button(text="Submit", command=getVals).grid()

root.mainloop()