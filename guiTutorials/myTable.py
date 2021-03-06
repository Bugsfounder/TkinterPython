from tkinter import *
from tkinter import font

def table():
    global tableFrame
    tableFrame.destroy()
    tableFrame = Frame(root)
    tableFrame.grid(row=2,pady=10, padx=10)
    try:
        l = Label(tableFrame, text=f"Table of: {int(tableVal.get())}", font="lucida 25 bold", fg='red')
        l.grid(row=3,column=2)
        for i in range(10):
            table = (i+1)* int(tableVal.get())
            t = Label(tableFrame, text=f"{int(tableVal.get())} X {int(i+1)} = {table}", font="lucida 20 bold", fg='blue', pady=5)
            t.grid(row=4+i, column=2) 
    except Exception as e:
        t = Label(tableFrame, text=f"Only Numbers are allowed", font="lucida 20 bold", fg='blue', pady=5)
        t.grid(row=4, column=2) 



# GUI STARTS HERE
root = Tk()
root.title("Manisha - MyTable") # GUI TITLE
root.geometry("470x600") # GUI HEIGHT WIDTH
root.minsize(470,300) # GUI MIN SIZE
# root.maxsize(600,1000) # GUI MIN SIZE

# CREATING VARIABLE FOR GET USER INPUT 
tableVal = StringVar()
frm = Frame(root) # CREATING A FRAME TO ADD INPUT FIELD AND BUTTON IN A ROW 
frm.grid(pady=10, padx=10)
# CREATING A ENTRY FOR TAKE INPUT 
tableEntry = Entry(frm, textvariable=tableVal, width=30, font="lucida 15 bold")
tableEntry.grid(row=1, column=2,padx=10)
# CREATING A BUTTTON 
Button(frm, text = "Get Table", fg='white', bg='blue', font="lucida 11 bold", command=table).grid(row=1, column=3)

tableFrame = Frame(root)
tableFrame.grid(row=2,pady=10, padx=10)



# GUI ENDS HERE
root.mainloop()