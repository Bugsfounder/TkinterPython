from tkinter import *


# GUI STARTS HERE
root = Tk()
root.title("Windows Layout - Manisha") # GUI TITLE
root.geometry("2000x2000") # GUI HEIGHT WIDTH
root.minsize(500,400) # GUI MIN SIZE

desktop = PhotoImage(file='bg.jpg')
desktopLabel = Label(image=desktop)
desktopLabel.pack()

# GUI ENDS HERE
root.mainloop()