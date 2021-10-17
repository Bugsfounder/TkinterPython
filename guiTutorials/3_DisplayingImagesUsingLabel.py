from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.title('Manisha The Genius')

root.geometry("700x500")
root.minsize(500,400)

imageManisha = PhotoImage(file='owner.png')
imageManishaLabel = Label(image=imageManisha)
imageManishaLabel.pack(pady=20)

manisha = Label( text = 'Manisha is a Genius Girl', font=("Monospace", 30, BOLD))
manisha.pack()


root.mainloop()