from tkinter import *


# GUI STARTS HERE
root = Tk()
root.title("Welcome To MyNoteBook - Manisha") # GUI TITLE
root.geometry("800x600") # GUI HEIGHT WIDTH
root.wm_iconbitmap('owner.ico')

welcomeFrame = Frame(root)
welcomeFrame.pack()

ownerImage = PhotoImage(file='owner.png')
ownerImageLabel = Label(welcomeFrame, image=ownerImage)
ownerImageLabel.pack(pady=20)

welcomeText = Label(welcomeFrame, text="Welcome to MyNotebook Created By Manisha", font="lucida 20 bold", fg='red')
welcomeText.pack()

# GUI ENDS HERE
root.mainloop()



