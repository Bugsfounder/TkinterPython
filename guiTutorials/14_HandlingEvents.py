from tkinter import *

def manisha(event):
    print(f"Button was Clicked at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry('500x400')


widget = Button(root, text="Click me Please")
widget.pack()

widget.bind('<Button-1>', manisha)
widget.bind('<Double-1>', quit)


root.mainloop()



