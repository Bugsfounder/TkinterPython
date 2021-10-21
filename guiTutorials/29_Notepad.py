import os
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename

#### FUNCTIONS ARE HERE
# FILE MENU FUNCTIONS HERE
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file  = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])

        if file=="":
            file = None
        else:
            #  SAVE AS NEW FILE 
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # SAVE THE FILE 
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

# EDIT MENU FUNCTIONS ARE HERE 
def cut():
    TextArea.event_generate('<<Cut>>')

def copy():
    TextArea.event_generate('<<Copy>>')

def paste():
    TextArea.event_generate('<<Paste>>')

# HELP MENU FUNCTIONS ARE HERE 
def about():
    tmsg.showinfo("About Notepad", "Notepad by Manisha")

if __name__ == "__main__":
    # GUI STARTS HERE
    root = Tk()
    root.title("Manisha Personal - Notepad") # GUI TITLE
    root.geometry("600x500") # GUI HEIGHT WIDTH

    # ADD TEXT AREA
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # LETS CREATE A MENU BAR 
    MenuBar = Menu(root)

    ## FILE MENU STARTS HERE 
    FileMenu = Menu(MenuBar, tearoff=0)
    
    # TO OPEN NEW FILE
    FileMenu.add_command(label="New", command=newFile)

    # TO OPEN AN ALREADY EXISTING FILE 
    FileMenu.add_command(label="Open", command=openFile)

    # TO SAVE CURRENT FILE 
    FileMenu.add_command(label="Save", command=saveFile)

    # ADDING SEPERATER
    FileMenu.add_separator()

    # TO EXIT THE NOTEPAD 
    FileMenu.add_command(label="Exit", command=quitApp)
    
    # ADDING NEW CASCADE TO MENUBAR CALLED FILEMENU
    MenuBar.add_cascade(label="File", menu=FileMenu)
    ## FILE MENU ENDS HERE 


    ## EDIT MENU STARTS HERE 
    EditMenu = Menu(MenuBar, tearoff=0)

    # TO GIVE FETURE OF CUT, COPY, PASTE
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    
    # ADDING NEW CASCADE TO MENUBAR CALLED EditMenu
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    ## EDIT MENU ENDS STARTS HERE 

    ## HELP MENU STARTS HERE
    HelpMenu = Menu(MenuBar, tearoff=0) 

    # ADDING HELP FETURE
    HelpMenu.add_command(label="About Notepad", command=about)

    # ADDING NEW CASCADE TO MENUBAR CALLED HELPMENU
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    ## HELP MENU ENDS HERER 


    # CONGIGURING MENU BAR OF ROOT CALLED MENUBAR 
    root.config(menu=MenuBar)


    # ADDING SCROLLBAR IN OUR NOTEPAD 
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    # GUI ENDS HERE
    root.mainloop()