# CREATE A GUI WINDOW WHICH TAKES AS INPUT WIDTH AND HEIGHT AND UPON CLICKING APPLY, IT SHOULD BE ABLE TO CHANGE ITS SIZE ACCORDINGLY

from os import close
from tkinter import *

# FUNCTION TO SET HEIGHT WIDHT CORRESPONDINT USER INPUT VALUES 
def setHeightWidth(event):
    root.geometry(f"{widthValue.get()}x{heightValue.get()}")
    
# GUI STARTS HERE 
root = Tk()
root.title("Exercise 2 Set Custom Height Width from user input") # GUI TITLE

# CREATING VARIABLES FOR HEIGHT WIDHT 
width = "800"
height = "600"

root.geometry(f"{width}x{height}")

# SETTING IMAGES 
myimage = PhotoImage(file='owner.png')
imgLabel = Label(image=myimage)
imgLabel.grid(pady=10,padx=10)

# CREATING LABEL FOR HEIGHT WIDTH 
setHeight = Label(root,text="Height")
setWidth = Label(root, text="Width")

# PACKING HEIGHT WIDTH LABEL 
setHeight.grid(row=1,pady=3)
setWidth.grid(row=3,pady=3)

# CREATING VARIABLES FOR STROE USERINPUT  
heightValue = StringVar()
widthValue = StringVar()

# CREATING ENTRIES FOR TAKE HEIGHT WIDTH FROM USER 
heightEntry = Entry(root, textvariable=heightValue)
widthEntry = Entry(root, textvariable=widthValue)

# PACKING ENTRIES HERE 
heightEntry.grid(row=2)
widthEntry.grid(row=4)

# CREATING BUTTON AND SETTING EVENTS ON BUTTON TO SET HEIGHT WIDTH OF THE WINDOW 
btn = Button(root, text="Apply Size")
btn.grid(pady=10)
btn.bind("<Button-1>", setHeightWidth)


root.mainloop()