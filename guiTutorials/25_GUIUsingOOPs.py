from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusBar = Label(self, textvariable=self.var, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button Clicked")

    def createButton(self, inptext):
        Button(text=inptext, command=self.click).pack()


class NoteBook(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

    def textBook(self):
        scroll = Scrollbar(self)
        scroll.pack(side=RIGHT, fill=Y)
        text =Text(self, yscrollcommand=scroll.set)
        text.pack(fill=BOTH)
        scroll.config(command=text.yview)


if __name__=="__main__":
    # window = GUI()
    # window.status()
    # window.createButton(inptext="My Btn")
    # window.mainloop()

    # Quick Quize 
    myGui = NoteBook()
    myGui.textBook()
    myGui.mainloop()