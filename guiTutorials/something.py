from tkinter import *

def openNew():
    root.destroy()
    # GUI STARTS HERE
    root2 = Tk()
    root2.title("can i open gui inside a gui") # GUI TITLE
    root2.geometry("600x500") # GUI HEIGHT WIDTH

    Button(root2, text='Click Me').pack()


    root2.mainloop()


# GUI STARTS HERE
root = Tk()
root.title("can i open gui inside a gui") # GUI TITLE
root.geometry("600x500") # GUI HEIGHT WIDTH

Button(root, text='Click Me', command=openNew).pack()

# GUI ENDS HERE
root.mainloop()

# question - can i open gui inside a gui
# answer - yes 