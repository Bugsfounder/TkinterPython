from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Recieved", f"We have Recieved Your Order For {var.get()}. Thanks for Ourdering")


# GUI STARTS HERE
root = Tk()
root.title("Radio Button Tutorial") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

# var = IntVar()
var = StringVar()
var.set("Radio")
Label(root, text="What would you like to eat?", justify=LEFT, font='lucida 19 bold', padx=14).pack()

# radio  = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa")
# radio.pack(anchor=W)

# radio  = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly")
# radio.pack(anchor=W)

# radio  = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha")
# radio.pack(anchor=W)

# radio  = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa")
# radio.pack(anchor=W)


lst = ["Dosa", "Dal", "Idly", "Chawal", "Roti", "Sabji"]
for i in range(len(lst)):
    radio = Radiobutton(root, text=lst[i], padx=14, variable=var, value=lst[i])
    radio.pack(anchor=W)

Button(text="Order Now", command=order).pack()

# GUI ENDS HERE
root.mainloop()