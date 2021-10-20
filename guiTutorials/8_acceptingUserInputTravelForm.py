from tkinter import *
from tkinter import font


def getVals():
    print("Submitting Form")
    with   open('records.txt', 'a') as f:
        f.write(f"{nameValue.get()}, {phoneValue.get()}, {genderValue.get()}, {emergencyContactValue.get()}, {paymentModeValue.get()}, {foodServiceValue.get()}\n")


root = Tk()

root.geometry('555x444')
root.title("Manisha is a Genius Girl")

# SETTING HEADING HERE 
Label(root, text="Welcome to Manisha Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# SETTING TEXT FOR OUR FORM
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergencyContact = Label(root, text="Emergency Contact")
paymentMode = Label(root, text="Payment Mode")

# PACKING TEXT FOR OUR FORM
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergencyContact.grid(row=4, column=2)
paymentMode.grid(row=5, column=2)

# CREATING VARIABLES FOR STORE ENTERIES OF OUR FORM
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyContactValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()

# CREATING ENTERIES FOR OUR FORM 
nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergencyContactEntry = Entry(root, textvariable=emergencyContactValue)
paymentModeEntry = Entry(root, textvariable=paymentModeValue)

# PACKING ENTERIES FOR OUR FORM
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyContactEntry.grid(row=4, column=3)
paymentModeEntry.grid(row=5, column=3)

# CHECKBOX AND PACKING IT
foodService = Checkbutton(text="Want to prebook your meals?", variable=foodServiceValue)
foodService.grid(row=6, column=3)

# BUTTON AND PACKING IT  AND ASSIGNING IT A COMMAND
Button(text="Submiy to Manisha Travels", command=getVals).grid(row=7, column=3)


root.mainloop()
