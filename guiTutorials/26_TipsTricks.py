from tkinter import *


# GUI STARTS HERE
root = Tk()
root.title("Tips and Tricks About Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH
# root.geometry("1366x768") # GUI HEIGHT WIDTH
root.wm_iconbitmap('favicon.ico')
root.configure(background="grey")


width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

# GUI ENDS HERE
root.mainloop()