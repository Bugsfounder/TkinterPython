from tkinter import *
from tkinter import font

root = Tk()

root.geometry('555x444')

Label(root, text="Welcome to Manisha Travels", font="comicsansms 13 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergencyContact = Label(root, text="Emergency Contact")
paymentMode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergencyContact.grid(row=4, column=2)
paymentMode.grid(row=5, column=2)

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyContactValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()


nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=nameValue)
genderEntry = Entry(root, textvariable=nameValue)
emergencyContactEntry = Entry(root, textvariable=nameValue)
paymentModeEntry = Entry(root, textvariable=nameValue)
foodServiceEntry = Entry(root, textvariable=nameValue)

nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyContactEntry.grid(row=4, column=3)
paymentModeEntry.grid(row=5, column=3)



root.mainloop()
