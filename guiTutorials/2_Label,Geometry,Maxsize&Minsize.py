from tkinter import *

manisha_root = Tk()

# WIDTH X HEIGHT
manisha_root.geometry("544x544")

# WIDTH, HEIGHT
manisha_root.minsize(400,400)

# WIDTH, HEIGHT 
manisha_root.maxsize(1000,600)

# lable 
manisha = Label(text="Manisha is a Most Successfull Person in The Whole World")
manisha.pack()


manisha_root.mainloop()