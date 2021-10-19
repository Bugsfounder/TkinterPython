from tkinter import *

def hello():
    print("Hello Manisha")

def name():
    print("Name is Manisha")

root = Tk()
root.geometry('655x333')

frame =Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
frame.pack(side=LEFT, anchor=NW)


b1 = Button(frame, fg = 'red', text="Print Now", command=hello)
b1.pack(side=LEFT, padx=10)

b2 = Button(frame, fg = 'red', text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=10)

b3 = Button(frame, fg = 'red', text="Print Now")
b3.pack(side=LEFT, padx=10)

b4 = Button(frame, fg = 'red', text="Print Now")
b4.pack(side=LEFT, padx=10)

b5 = Button(frame, fg = 'red', text="Print Now")
b5.pack(side=LEFT, padx=10)

b6 = Button(frame, fg = 'red', text="Print Now")
b6.pack(side=LEFT)

b7 = Button(frame, fg = 'red', text="Print Now")
b7.pack(side=LEFT, padx=10)

root.mainloop()