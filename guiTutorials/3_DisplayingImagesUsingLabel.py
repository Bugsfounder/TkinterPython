from tkinter import *
import tkinter

root = Tk()

root.geometry("600x500")

image = tkinter.Image(name='owner.png', imgtype='photo', height=500, width=500)

manisha = Label(text='Manisha is a Genius Girl', font=('Monospace', 25))
manisha.pack(padx=20,pady=78)




root.mainloop()

