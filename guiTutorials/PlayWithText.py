from operator import le
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg


# FUNCTIONS ARE HERE 
def capitalizeEachWord(text):
    textr = text.split(" ")
    returnText = ""
    for i in range(len(textr)):
        returnText += textr[i].capitalize() + " "

    return returnText 


def click(event):
    global userText, userTextResult, file
    text = event.widget.cget("text")
    val = 'empty'

    if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
        newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), " ")

    if text == "Capitalize":
        userTextResult.delete(1.0, END)
        val = newVal.capitalize() + ''
        userTextResult.insert(0.0, val )

    elif text == "Upper Case":
        userTextResult.delete(1.0, END)
        val =  newVal.upper()+''
        userTextResult.insert(0.0, val)

    elif text == "Lower Case":
        userTextResult.delete(1.0, END)
        val = newVal.lower()+''
        userTextResult.insert(0.0, val)

    elif text == "Cap Each Word":
        userTextResult.delete(1.0, END)
        val =  capitalizeEachWord(newVal) + ''
        userTextResult.insert(0.0, val)

    elif text == "Copy":
        copy()

    elif text == "Cut":
        cut()

    elif text == "Paste":
        paste()

    elif text == "Delete":
            if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
                newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), "")
                userTextResult.delete(1.0, END)
                userText.delete(1.0, END)

    elif text == "Save":
        # global file 
        # if file == None:
        #     file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        #     if file == "":
        #         file= None
        #     else:
        #         # SAVE AS NEW FILE 
        #         f = open(file, 'w')
        #         f.write(userTextResult.get(1.0, END))
        #         f.close()
        # else:
        #     # SAVE THE FILE 
        #     f = open(file, 'w')
        #     f.write(userTextResult.get(1.0, END))
        #     f.close()

        saveFile()
    elif text == "Open":
          openFile()()


# MENUBAR FUNCTIONS ARE HERE 
# FUNCTION FOR CHANGE THEME 
def shiftMode(event):
    global modeBtnsFrame, modeBtns, allBtns
    mode = event.widget.cget("text")
    if mode == "Enable Relax Mode":
        purpleTheme()
    elif mode == "Enable Light Mode":
        lightTheme()

# FUNCTION FOR OPEN A NEW BLANK FILE
def newFile():
    if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
            newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), "")
            userTextResult.delete(1.0, END)
            userText.delete(1.0, END)

# FUNCTION TO OPEN AN EXISTING FILE 
def openFile():
    global file
    file  = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        userText.delete(1.0, END)
        f = open(file, 'r')
        userText.insert(1.0, f.read())
        f.close()

# FUNCTION FOR OPEN A FILE 
def saveFile():
    global file
    if file == None:
        if file=="":
            file = None
        if len(userTextResult.get(1.0, END)) > 1:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
            #  SAVE AS NEW FILE 
            f = open(file, 'w')
            f.write(userTextResult.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
        else:
            msg = tmsg.askokcancel(title="Actions Box Was Empty", message="Action Box was Empty You want to save you origional content")
            print(msg)
            if msg == True:
                file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
                #  SAVE AS NEW FILE 
                f = open(file, 'w')
                f.write(userText.get(1.0, END))
                root.title(os.path.basename(file) + " - Notepad")
                f.close()
    else:
        # SAVE THE FILE  
        f = open(file, 'w')
        f.write(userTextResult.get(1.0, END))
        print(userTextResult.get(1.0, END), 2)
        f.close()
      

# FUNCTION FOR CUT 
def cut():
    userText.event_generate('<<Cut>>')

# FUNCTION TO COPY 
def copy():
    userText.event_generate('<<Copy>>')

# FUNCTION TO PASTE 
def paste():
    userText.event_generate('<<Paste>>')

# FUNCTION TO UNDO 
def undo():
    userText.event_generate('<<Undo>>')

# FUNCTION FOR REDO 
def redo():
    userText.event_generate('<<Redo>>')

# FUNCTION FOR PURPLE THEME 
def purpleTheme():
    global btnColor
    btnColor = '#3b2664'
    root.configure(background="#3b2664")
    heading.configure(background='#3b2664', fg='white')
    modeBtnsFrame.config(bg='#3b2664')
    screenFrame.config(bg='#3b2664')
    userText.configure(background='#664a9d', fg='white')
    userTextResult.configure(background='#664a9d', fg='white')
    buttonFrame.config(bg='#3b2664')

# FUNCTION FOR LIGHT THEME 
def lightTheme():
    root.configure(background="white")
    heading.configure(background='white', fg='#3e1d7e')
    modeBtnsFrame.config(bg='white')
    screenFrame.config(bg='white')
    userText.configure(background='white', fg='black')
    userTextResult.configure(background='white', fg='black')
    buttonFrame.config(bg='white')

# FUNCTION FOR DARK THEME 
def darkTheme():
    global btnColor
    btnColor = 'black'
    root.configure(background="black")
    heading.configure(background='black', fg='white')
    modeBtnsFrame.config(bg='black')
    screenFrame.config(bg='black')
    userText.configure(background='grey', fg='white')
    userTextResult.configure(background='grey', fg='white')
    buttonFrame.config(bg='black')

# FUNCTION FOR RED THEME 
def redTheme():
    global btnColor
    btnColor = '#870000'
    root.configure(background="#870000")
    heading.configure(background='#870000', fg='white')
    modeBtnsFrame.config(bg='#870000')
    screenFrame.config(bg='#870000')
    userText.configure(background='#b51f1f', fg='white')
    userTextResult.configure(background='#b51f1f', fg='white')
    buttonFrame.config(bg='#870000')

# FUNCTION FOR ABOUT IN HELP MENU 
def about():
    tmsg.showinfo(title="About Software", message="You can use this software for manipuating text in between your work sometimes you have to manipulate text like convert all text into lowercase and uppercase etc and you can do this manually and you also know it is a big headech to you can use this software to do these thing perfectly and in a good manner. Thanks for using my software")

if __name__ == '__main__':

    # GUI STARTS HERE
    root = Tk()
    root.title("Manisha - Play With Text") # GUI TITLE
    root.geometry("830x700") # GUI HEIGHT WIDTH
    root.minsize(500,400) # GUI MIN SIZE

    file = None
    # ADDING MENU BAR HERE 
    menuBar = Menu(root)
    # CREATING FILE MENU HERE WITH NEWFILE, OPENFILE, SAVEFILE FUNCTIONALITIES
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)

    # CREATING EDITMENU HERE WITH CUT, COPY, PASTE, UNDO, REDO FUNCTIONALITIES 
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    editMenu.add_separator()
    editMenu.add_command(label="Undo", command=undo)
    editMenu.add_command(label="Redo", command=redo)

    # CREATING THEME MENU WITH SOME COLORED THEMES 
    themeMenu = Menu(menuBar, tearoff=0)
    themeMenu.add_command(label="Light Theme",  command=lightTheme)
    themeMenu.add_command(label="Dark Theme", command= darkTheme)
    themeMenu.add_command(label="Red Theme", command= redTheme)
    themeMenu.add_command(label="Purple Theme", command= purpleTheme)

    # CREATING HELP MENU WITH ABOUR APP 
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=about)

    # ADDING ALL CASCADES TO MAIN MANUBAR 
    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    menuBar.add_cascade(label="Theme", menu=themeMenu)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    # CONFIGURING MENUBAR FOR ROOT 
    root.config(menu=menuBar)

    # HEADING OF THE APP 
    heading = Label(root, text="Welcome to Play With Text By Manisha", font="lucida 15 bold", fg='#3e1d7e')
    heading.pack(pady=5)

    # CREATING FRAMES FOR SWITCH THEMES 
    modeBtnsFrame = Frame(root, )
    modeBtnsFrame.pack()

    # STORING ALL BUTTONS NAME IN AN ARRAY  
    modeBtns = ["Enable Relax Mode", "Enable Light Mode"]

    # CREATING ALL BUTTON USING FOR LOOP 
    for  i in range(len(modeBtns)):
        btnColor = '#656572'
        modeBtn = Button(modeBtnsFrame, text=f"{modeBtns[i]}", font="lucida 10 bold", bg=f'{btnColor}', fg='white')
        modeBtn.pack(pady=15, padx=10, side=LEFT)
        modeBtn.bind("<Button-1>", shiftMode)

    # CREATING SCREEN FRAME FOR TAKING USERS TEXT AND RETURNING TEXT 
    screenFrame = Frame(root)
    screenFrame.pack()

    # CREAING A TEXTAREA FOR USER TEXT 
    userText = Text(screenFrame, font="lucida 14", width=35, height=15)
    userText.pack(padx=10, side=LEFT)

    # CREATING A TEXTAREA FOR RESULT TEXT 
    userTextResult = Text(screenFrame, font="lucida 14", width=35, height=15)
    userTextResult.pack(padx=10, side=LEFT)

    # CREATING A BUTTON FRAME TO ALL ACTIONS 
    buttonFrame =Frame(root)
    buttonFrame.pack()

    # STORING ALL BUTTONS NAME IN A LIST 
    allBtns = ["Capitalize", "Upper Case", "Lower Case", "Cap Each Word" ,"Copy", "Cut", "Paste", "Save","Open", "Delete"]

    # CREAING ALL BUTTON USING FOR LOOP 
    for  i in range(len(allBtns)):
        btnColor = '#656572'
        capitalizeBtn = Button(buttonFrame, text=f"{allBtns[i]}", font="lucida 10 bold", bg=f'{btnColor}', fg='white')
        capitalizeBtn.pack(pady=30, padx=10, side=LEFT)
        capitalizeBtn.bind("<Button-1>", click)


    # GUI MAIN LOOP HERE 
    root.mainloop()