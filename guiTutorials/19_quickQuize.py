from tkinter import *

def rate():
    with open("rate.txt", 'a')as r:
        r.write(f"Name: {nameValue.get()}\nRated: {ratingsChart.get()}\n")

# GUI STARTS HERE
root = Tk()
root.title("Customer Rating") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

heading = Label(text="Rate Us")
heading.pack(pady=10)
name = Label(text="Enter Your Name")
name.pack()
nameValue = StringVar()
nameEntry = Entry(root, textvariable=nameValue)
nameEntry.pack()

ratingsChart = Scale(root, from_=0, to=10, orient=HORIZONTAL)
ratingsChart.pack()

Button(root, text="Rate", command=rate).pack(pady=20)


# GUI ENDS HERE
root.mainloop()