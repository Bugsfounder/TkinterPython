from tkinter import *
import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
dbName = client['myNotebook']

class Backend():
    global username
    allAvailableCollections = dbName.list_collection_names()
    userCollection = dbName['users']
    notebookCollection = dbName['notebooks']
    noteCollection = dbName['notes']
    timestamp =  datetime.datetime.utcnow()
    notebookOwnerName = ""
    notebookOwnerPassword = ""
    NoteBookName = ""
    NotebookOwnerImage = "owner.png"
    entryHeight = 5
    entryWidth = 30
    btnWidth = 29
    bgColor = "0e1d4e"
    
    # USERS COLLECTIONS FUNCTIONS 
    # GET ALL COLLECTIONS 
    def allCollections(self):
        for collection in self.allAvailableCollections:
            print(collection)

    # CREATE A NEW USER FUNCTION 
    def createNewUser(self):
        userCol = self.userCollection
        newDoc = {
            "email": f"{email.get()}",
            "name": f"{username.get()}",
            "password": f"{password.get()}",
            "timestamp":{"$timestamp": self.timestamp}
        }
        isExists = userCol.count_documents({"email":f"{email.get()}"})
        if isExists == 0 and len(email.get())>5:
            userCol.insert_one(newDoc)
            print("Account Created Successfully")
        else:
            print("This email Already Exists, Email must be greater than 5 characters")

    # CREATING SIGNUP PAGE GUI
    def signup(self):
        # DESTRY THE ROOT WINDOW 
        root.destroy()
        # CREATING A NEW GUI WINDOW FOR TAKE USERNAME OR PASSWORD OF HIS/HER NOTEBOOK
        createNewUser = Tk()
        createNewUser.title("Creating New Notebook") # GUI TITLE
        createNewUser.geometry("800x600") # GUI HEIGHT WIDTH
        
        # CREATING USER FRAME 
        userFrame = Frame(createNewUser)
        userFrame.pack()

        # CREATING TITLE LABEL
        welcomeText = Label(userFrame, text="Welcome to MyNotebook Created By Manisha", font="lucida 20 bold", fg='#0e1d4e')
        welcomeText.pack(pady=10)

        # CREATING DESCRIPTION LABEL
        welcomeText = Label(userFrame, text="Fill all black fields to create a new notebook", font="lucida 10", fg='#0e1d4e')
        welcomeText.pack()

        # CREATING LABEL 
        usernameLabel = Label(userFrame, text="Enter Your Name", font="lucida 12")
        usernameLabel.pack()
        # CREATING ENTRY  FOR TAKE USERNAME 
        print("Hello")
        usernameEntry = Entry(userFrame, textvariable=username, font="lucida 12", width=self.entryWidth )
        usernameEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING LABEL 
        emailLabel = Label(userFrame, text="Enter Your Email", font="lucida 12")
        emailLabel.pack()
        # CREATING ENTRY  FOR TAKE USERNAME 
        emailEntry = Entry(userFrame, textvariable=email, font="lucida 12", width=self.entryWidth )
        emailEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING LABEL 
        passwordLabel = Label(userFrame, text="Enter Password", font="lucida 12")   
        passwordLabel.pack()
        # CREATING ENTRY FOR TAKE PASSWORD 
        passwordEntry = Entry(userFrame, textvariable=password, font="lucida 12", width=self.entryWidth)
        passwordEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING BUTTON FOR CREATE A NEW NOTEBOOK 
        Button(userFrame, text="Create", font="lucida 12", width=self.btnWidth, bg='#0e1d4e', fg='white', command=self.createNewUser).pack(pady=10, ipady=3, ipadx=3)
        
        # GUI ENDS HERE
        createNewUser.mainloop()
      
    # FIND A USER IF EXISTS 
    def login(self):
        userCol = self.userCollection
        newDoc = {
            "email": f"{email.get()}",
            "name": f"{username.get()}",
            "password": f"{password.get()}"
            # "timestamp":{"$timestamp":{self.timestamp}}
        }
        allDocs = userCol.find_one(newDoc)
        if userCol.find_one(newDoc):
            return True
        else:
            return False

    # FIND A USER IF EXISTS 
    def findUser(self):
        userCol = self.userCollection
        newDoc = {
            "email": f"{email.get()}",
            "name": f"{username.get()}",
            "password": f"{password.get()}"
            # "timestamp":{"$timestamp":{self.timestamp}}
        }
        allDocs = userCol.find_one(newDoc)
        if userCol.find_one(newDoc):
            return True
        else:
            return False

    # UPDATE A USER 
    def updateUser(self):
        userCol = self.userCollection
        try:
            newDoc = {
                "email": f"{email.get()}",
                "name": f"{username.get()}",
                "password": f"{password.get()}"
                # "timestamp":{"$timestamp":{self.timestamp}}
            }
            allDocs = userCol.find_one()
            print(allDocs)
            # UPDATE MANY 
            prev = {"name":f"{allDocs['name']}", "email":f"{allDocs['email']}", "password":f"{allDocs['password']}" }
            nextupdated = {'$set': newDoc}
            up = userCol.update_one(prev, nextupdated)
            print(up.modified_count)
        except Exception as e:
            print(e)
            print("Something went wrong")

    # DELETE A USER 
    def deleteUser(self):
        userCol = self.userCollection
        newDoc = {
            "name": f"{username.get()}",
            "email": f"{email.get()}",
            "password": f"{password.get()}",
        }
        isExists = userCol.count_documents({"email":f"{email.get()}"})
        print(isExists)
        if isExists > 0:
            self.userCollection.delete_one(newDoc)
        else:
            print("This user not Exists")

    # NOTEBOOK FUNCTIONS ARE HERE 
    # CREATE A NEW NOTEBOOK 
    def createNotebook(self):
        pass

    # SEARCH NOTEBOOKS 
    def searchNotebooks(self):
        pass

    # SEARCH NOTEBOOK 
    def searchNotebook(self):
        pass

    # UPDATE NOTEBOOK 
    def updateNotebook(self):
        pass

    # DELETE NOTEBOOK 
    def deleteNotebook(self):
        pass


class NoteBook():
    notebookOwnerName = ""
    notebookOwnerPassword = ""
    NoteBookName = ""
    NotebookOwnerImage = "owner.png"
    entryHeight = 5
    entryWidth = 30
    btnWidth = 29
    bgColor = "0e1d4e"

    def createNewNotebook(self):
        # DESTRY THE ROOT WINDOW 
        root.destroy()
        # CREATING A NEW GUI WINDOW FOR TAKE USERNAME OR PASSWORD OF HIS/HER NOTEBOOK
        NewNoteBook = Tk()
        NewNoteBook.title("Creating New Notebook") # GUI TITLE
        NewNoteBook.geometry("800x600") # GUI HEIGHT WIDTH
        
        # CREATING USER FRAME 
        userFrame = Frame(NewNoteBook)
        userFrame.pack()

        # DISPLAYING USERIMAGE HERE
        # userimage = PhotoImage(file=self.NotebookOwnerImage)
        # userimageLabel = Label(userFrame, image=userimage)
        # userimageLabel.pack(pady=10)

        # CREATING TITLE LABEL
        welcomeText = Label(userFrame, text="Welcome to MyNotebook Created By Manisha", font="lucida 20 bold", fg='#0e1d4e')
        welcomeText.pack(pady=10)

        # CREATING DESCRIPTION LABEL
        welcomeText = Label(userFrame, text="Fill all black fields to create a new notebook", font="lucida 10", fg='#0e1d4e')
        welcomeText.pack()


        # CREATING LABEL 
        usernameLabel = Label(userFrame, text="Enter Your Name", font="lucida 12")
        usernameLabel.pack()
        # CREATING ENTRY  FOR TAKE USERNAME 
        usernameEntry = Entry(userFrame, textvariable=userName, font="lucida 12", width=self.entryWidth )
        usernameEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING LABEL 
        usernameLabel = Label(userFrame, text="Enter Notebook Name", font="lucida 12")
        usernameLabel.pack()
        # CREATING ENTRY FOR TAKE NOTEBOOK NAME 
        notebookNameEntry = Entry(userFrame, textvariable=notebookName, font="lucida 12", width=self.entryWidth )
        notebookNameEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING LABEL 
        usernameLabel = Label(userFrame, text="Enter Password", font="lucida 12")   
        usernameLabel.pack()
        # CREATING ENTRY FOR TAKE PASSWORD 
        passwordEntry = Entry(userFrame, textvariable=password, font="lucida 12", width=self.entryWidth)
        passwordEntry.pack(ipadx=2, ipady=2, pady=8)

        # CREATING BUTTON FOR CREATE A NEW NOTEBOOK 
        Button(userFrame, text="Create", font="lucida 12", width=self.btnWidth, bg='#0e1d4e', fg='white').pack(pady=10, ipady=3, ipadx=3)
        
        # GUI ENDS HERE
        NewNoteBook.mainloop()

    def openExistingNotebook(self):
        pass



if __name__ == "__main__":

    notebook = NoteBook()
    db = Backend()



    # GUI STARTS HERE
    root = Tk()
    root.title("Welcome To MyNoteBook - Manisha") # GUI TITLE
    root.geometry("800x600") # GUI HEIGHT WIDTH
    
    # SPCIFIC VARIABLES 
    # VARIABLES FOR USER ACCOUNT 
    username  = StringVar()
    email  = StringVar()
    password  = StringVar()

    # CREATING VARIABLE TO STORE USERNAME OR PASSWORD NOTEBOOK
    userName = StringVar()
    notebookName = StringVar()
    password = StringVar()

    # VARIABLES FOR NOTES 
    notebookNameInNotes = StringVar()
    notebookOwnerName  = StringVar()
    noteTitle = StringVar()
    noteDescription = StringVar()

    welcomeFrame = Frame(root)
    welcomeFrame.pack()

    ownerImage = PhotoImage(file='owner.png')
    ownerImageLabel = Label(welcomeFrame, image=ownerImage)
    ownerImageLabel.pack(pady=20)

    welcomeText = Label(welcomeFrame, text="Welcome to MyNotebook Created By Manisha", font="lucida 20 bold", fg='#3e1d7e')
    welcomeText.pack()

    welcomeDescription = Label(welcomeFrame, text="Welcome to MyNotebook Created By Manisha Welcome to MyNotebook Created By Manisha\n Welcome to MyNotebook Created By Manisha Welcome to MyNotebook\n Created By Manisha Welcome to MyNotebook Created By Manisha\n Welcome to MyNotebook Created By Manisha", font="lucida 10", fg='#3e1d7e')
    welcomeDescription.pack()

    Button(welcomeFrame, text="Create New Account", command=db.signup).pack(pady=10)
    Button(welcomeFrame, text="Already Have a Account", command=db.login).pack()

    # GUI ENDS HERE
    root.mainloop()



