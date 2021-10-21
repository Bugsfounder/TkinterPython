from tkinter import *
from tkinter import font

def click(event):
    global calculateValue
    text = event.widget.cget("text")
    if text=="=":
        if calculateValue.get().isdigit():
            value = int(calculateValue.get())
        else:
            try:
                value = eval(calculateValueEntry.get())
            except Exception as error:
                print(error)
                value = "Wrong Expression"

        calculateValue.set(value)
        calculateValueEntry.update()
    
    elif text=="C":
        calculateValue.set("")
        calculateValueEntry.update()
    else:
        calculateValue.set(calculateValue.get()+text)
        calculateValueEntry.update()

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

    elif text == "C":
        calculateValue.set("")
        calculateValueEntry.update()
    else:
        calculateValue.set(calculateValue.get()+text)
        calculateValueEntry.update()



# GUI STARTS HERE
root = Tk()
root.title("Manisha Personal - Calculator") # GUI TITLE
root.geometry("500x600") # GUI HEIGHT WIDTH
root.minsize(400,400) # GUI MIN SIZE
root.maxsize(600,700) # GUI MAX SIZE

inputFrame = Frame(root)
inputFrame.grid(pady=10, padx=7)
calculateValue = StringVar()

calculateValueEntry = Entry(inputFrame, fg='white', bg='blue', textvariable=calculateValue, font="lucida 20 bold", width=32)
calculateValueEntry.grid(row=1, column=1)

keybord = Frame(root, bg='blue')
keybord.grid(row=2, column=0)

btnv = 9
symbolBtn = ['C', "=" , "%", "/", "*", "-", "+", ".", "0" ]
sBtnV = len(symbolBtn)-1

for row in range(6):
    for column in range(3):
        if btnv not in symbolBtn and btnv > 0:
            Btn = Button(keybord,  padx=27, text=f"{btnv}", font="lucida 25 bold", width=4, height=1, fg='white',bg='black')
            Btn.grid(row=row, column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            btnv = btnv-1
        else:
            Btn = Button(keybord,  padx=27, text=f"{symbolBtn[sBtnV]}", font="lucida 25 bold", width=4, height=1, fg='white',bg='black')
            Btn.grid(row=row, column=column, padx=10, pady=10)
            Btn.bind("<Button-1>", calculate)
            sBtnV = sBtnV - 1


# GUI ENDS HERE
root.mainloop()