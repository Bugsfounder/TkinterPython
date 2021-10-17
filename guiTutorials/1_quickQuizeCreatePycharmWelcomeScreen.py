from tkinter import *

root = Tk()

root.geometry("733x434")
welcome = Label(text="Pycharm Community Edition", font=('monospace', 25))
welcome.pack(pady=20)

create = Label(text="+ Create New Project")
create.pack()

open = Label(text="☻ Open")
open.pack()

checkOut = Label(text="- Check Out From Version Control ^")
checkOut.pack()

root.mainloop()