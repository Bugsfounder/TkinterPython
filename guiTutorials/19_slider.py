from tkinter import *
import tkinter.messagebox as tmsg


# GUI STARTS HERE
root = Tk()
root.title("Slider in Python Using Tkinter") # GUI TITLE
root.geometry("500x400") # GUI HEIGHT WIDTH

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()

def getDollor():
    print(f"We have credited {myslider2.get()} dollors in your backaccount")
    tmsg.showinfo("Credited",f"We have credited {myslider2.get()} dollors in your backaccount")

Label(root, text="How Many Dollors You Want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(30)
myslider2.pack()
Button(root, text="Get Dollors!", command=getDollor).pack()




# GUI ENDS HERE
root.mainloop()