from tkinter import *
from tkinter import font

def start(event):
    print("Hello it is started")
    startmenuLabel = Label(root,image=startmenu,)
    startmenuLabel.pack(side=BOTTOM)


# GUI STARTS HERE
root = Tk()
root.title("Windows Layout - Manisha") # GUI TITLE
root.geometry("600x500") # GUI HEIGHT WIDTH
root.minsize(500,400) # GUI MIN SIZE




win = PhotoImage(file='icons.png')
taskbarPlate = Label(root, image=win)
taskbarPlate.bind("<Button-1>", start)
taskbarPlate.pack(side=BOTTOM, fill=X)

startmenu = PhotoImage(file='startmenu.png')

# imageManisha = PhotoImage(file='bg.png',  width=700, height=600)
# imageManishaLabel = Label(image=imageManisha,)
# imageManishaLabel.pack(pady=20)
# GUI ENDS HERE
root.mainloop()