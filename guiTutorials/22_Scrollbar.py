from tkinter import *


# GUI STARTS HERE
root = Tk()
root.title("Scroll Bar in Python GUI Using Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

# FOR CONNECTING SCROLLBAR TO A WIDGET 
# 1. widget(yscrollcommand = scrollbar.set)
# 2. Scrollbar.config(command=Widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox  = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(300):
#     listbox.insert(END, f"Item {i}")

# listbox.pack(fill=BOTH, padx=22)
# scrollbar.config(command=listbox.yview)

# text =Text(root, yscrollcommand=scrollbar.set)
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)


# GUI ENDS HERE
root.mainloop()