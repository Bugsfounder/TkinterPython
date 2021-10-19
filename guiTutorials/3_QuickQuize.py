from tkinter import *
from tkinter import font


root = Tk()

root.geometry('500x400')

root.title("Exercise from Harry Bhai")

pageTitle = Label(text="Program is Ready", font=("", 25, 'bold'), pady=50)
pageTitle.pack()

strip = Label(text="Ready", bg='black', fg='white', font=("", 9, 'bold'))
strip.pack(side=BOTTOM, fill=X)


root.mainloop()