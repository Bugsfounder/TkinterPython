from tkinter import *

def upload():
    statusVar.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    statusVar.set("Ready")



# GUI STARTS HERE
root = Tk()
root.title("Status Bar In Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH


statusVar = StringVar()
statusVar.set("Ready")
sbar = Label(root, textvariable=statusVar, relief=SUNKEN, anchor=W, padx=10)
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

# GUI ENDS HERE
root.mainloop()