from tkinter import *
from tkinter import font
import time

def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        if calculateValue.get().isdigit():
            value = int(calculateValue.get())
        else:
            try: 
                value = eval(calculateValueEntry.get())
            except Exception as e:
                value = "Wrong Expression"
                calculateValue.set(value)
                calculateValueEntry.update()
                time.sleep(1)
                value = ""
                calculateValue.set(value)
                calculateValueEntry.update()
        calculateValue.set(value)
        calculateValueEntry.update()
    elif text == "C":
        calculateValue.set("")
        calculateValueEntry.update()
    elif text == "««":
        val = calculateValue.get()
        setVal = val[:len(val)-1]
        calculateValue.set(setVal)
        calculateValueEntry.update()
    else:
        calculateValue.set(calculateValue.get()+text)
        calculateValueEntry.update()

# GUI STARTS HERE
root = Tk()
root.title("Manisha Personal - Calculator") # GUI TITLE
root.geometry("600x700") # GUI HEIGHT WIDTH
root.minsize(400,400) # GUI MIN SIZE
root.maxsize(500,610) # GUI MAX SIZE

inputFrame = Frame(root)
inputFrame.grid(pady=10, padx=7)
calculateValue = StringVar()

calculateValueEntry = Entry(inputFrame, fg='white', bg='#e500b4', textvariable=calculateValue,  font="lucida 20 bold", width=32)
calculateValueEntry.grid(row=1, column=1, ipady=10)

keybord = Frame(root, bg='#e500b4')
keybord.grid(row=2, column=0)

btnv = 9
symbolBtn = ['C', "=" , "««", "/", "*", "-", "+", ".", "0" ]
sBtnV = len(symbolBtn)-1

for row in range(6):
    for column in range(3):
        if btnv not in symbolBtn and btnv > 0:
            Btn = Button(keybord,  padx=27, text=f"{btnv}", font="lucida 25 bold", width=4, height=1, fg='white',bg='#640058')
            Btn.grid(row=row, column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            btnv = btnv-1
        else:
            Btn = Button(keybord,  padx=27, text=f"{symbolBtn[sBtnV]}", font="lucida 25 bold", width=4, height=1, fg='white',bg='#640058')
            Btn.grid(row=row, column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            sBtnV = sBtnV - 1

# GUI ENDS HERE
root.mainloop()