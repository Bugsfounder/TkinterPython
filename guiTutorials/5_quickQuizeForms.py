from tkinter import *

def submitForm():
    try:
        formText = f"Username: {usernameValue.get()}\nEmail: {emailValue.get()}\nPhone Number: {phoneValue.get()}\nPassword: {passwordValue.get()}\n\n\n"
        with open('form.txt', 'at') as form:
            form.write(formText)
    except Exception as error:
        print("Form has not been submitted for some reson please try again.")
# GUI Starts here 
root = Tk()
root.geometry('600x500')
root.title("Manisha Dance Class Form Submition")

# seting tile of the page 
title = Label(text="Welcomet to Manisha Dance Class", font=("", 25, 'bold'), fg='Blue')
title.grid()

# creating a frame 
form = Frame(root)
form.grid()

# labels for inputs 
username = Label(form, text="Username")
email = Label(form, text="Email Id")
phone = Label(form, text="Phone Number")
password = Label(form, text="Password")

username.grid(row=1, pady=10)
email.grid(row=2, pady=10)
phone.grid(row=3, pady=10)
password.grid(row=4, pady=10)

# creating varialbes to get user information 
usernameValue = StringVar()
emailValue = StringVar()
phoneValue = StringVar()
passwordValue = StringVar()

# creating entries for form 
nameEntry = Entry(form, textvariable=usernameValue)
emailEntry = Entry(form, textvariable=emailValue)
phoneEntry = Entry(form, textvariable=phoneValue)
passworsEntry = Entry(form, textvariable=passwordValue)

# packing enteries into form 
nameEntry.grid(row=1, column=1, pady=10)
emailEntry.grid(row=2, column=1, pady=10)
phoneEntry.grid(row=3, column=1, pady=10)
passworsEntry.grid(row=4, column=1, pady=10)

# creating button for taking action while submitting the form 
btn = Button(form, text="Submit", command=submitForm).grid()

root.mainloop()
# GUI Ends Here 