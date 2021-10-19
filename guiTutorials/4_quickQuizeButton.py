from tkinter import *


# functions are here 
def button1():
    print("This button number 1")

def button2():
    print("This button number 2")

def button3():
    print("This button number 3")

def button4():
    print("This button number 4")



# GUI starts here 
root = Tk()
root.geometry("500x400")

# frames here 
f1 = Frame(root, borderwidth=6, bg='blue', relief=SUNKEN)
f1.pack(pady=140)


# buttons Here 
button1 = Button(f1, text="Print Something", fg='white', font=("", 10, "bold"), bg="red", command=button1)
button1.pack(padx=3, side=LEFT)

button2 = Button(f1, text="Print Something", fg='white', font=("", 10, "bold"), bg="red", command=button2)
button2.pack(padx=3, side=LEFT)

button3 = Button(f1, text="Print Something", fg='white', font=("", 10, "bold"), bg="red", command=button3)
button3.pack(padx=3, side=LEFT)

button4 = Button(f1, text="Print Something", fg='white', font=("", 10, "bold"), bg="red" , command=button4)
button4.pack(padx=3, side=LEFT)


root.mainloop()
# GUI Ends here