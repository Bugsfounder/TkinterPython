from tkinter import *
from tkinter.font import BOLD

def click(event):
    global scValue
    text = event.widget.cget("text")
    if text=="=":
        if scValue.get().isdigit():
            value  = int(scValue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as error:
                value = "Error"
        
        scValue.set(value)
        screen.update()

    elif text=="C":
        scValue.set("")
        screen.update()
    else:
        scValue.set(scValue.get()+text)
        screen.update()




# GUI STARTS HERE
root = Tk()
root.title("Manisha Personal Calculator") # GUI TITLE
root.geometry("500x700") # GUI HEIGHT WIDTH

scValue = StringVar()
scValue.set("")
screen = Entry(root, textvariable=scValue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=5, pady=5, padx=20)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=20, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0", padx=21.4, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=21.4, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=21.4, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()



f = Frame(root, bg="grey")
b = Button(f, text="*", padx=22, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=22, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=22, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="%", padx=18, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=19, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="10", padx=12, pady=5, font="lucida 30 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)
f.pack()

keyBoard1 = Frame(root)
keyBoard1.pack()




# for i in range(3):
#     keyBoard = Frame(root)
#     keyBoard.pack()
#     j = 3
#     v = 9
#     if v>7:
#         while v!=6:
#             key = Button(keyBoard, text=f"{v}", padx=20, font="lucida 25 bold")
#             key.pack(side=LEFT)
#             key.bind("<Button-1>", click)
#             v = v-1
#     elif v>4:
#         c=6
#         while c!=3:
#             key = Button(keyBoard, text=f"{c}", padx=20, font="lucida 25 bold")
#             key.pack(side=LEFT)
#             key.bind("<Button-1>", click)
#             c = c-1
# GUI ENDS HERE
root.mainloop()