# Libraries
from tempfile import NamedTemporaryFile
import shutil
import csv
import tkinter as tk
import hashlib

FILE = "database.csv"

TEXT1 = ("Verdana", 12)
TEXT2 = ("Arial", 12)


class PasswordManager(tk.Tk):  # Passes the Root from later on to activate the class

    def __init__(self, *args, **kwargs):  # Initialises the arguments and key arguments in the class
        tk.Tk.__init__(self, *args, **kwargs)  # The root will also initialise the arguments and key arguments
        container = tk.Frame(self)  # Creates a "base frame" as the container
        container.pack(side="top", fill="both",
                       expand=True)  # Fill argument fills in space allocated, and expand just expands it
        container.grid_rowconfigure(0, weight=1)  # Used for priority of GUI (like infront of behind)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Used as a library, will be used in future to change frame

        for F in (Login, Register, Session):
            frame = F(container, self)
            self.frames[F] = frame  # Basically it makes the "login frame" the main frame, and "brings" it to the front
            frame.grid(row=0, column=0,
                       sticky="nsew")  # Sticky just makes it so it stretches to all directions with expand attribute
            frame.config(bg="#246587")

        self.showFrame(Login)

    def showFrame(self, cont):  # Cont just a parameter for frame
        frame = self.frames[cont]
        frame.tkraise()  # Makes the frame visible, hides others.


class Login(tk.Frame):  # Inherits Frame as it's unique

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # Initialises the frame's attributes

        loginText = tk.Label(self, text="Login", width=20, pady=50, font=TEXT1, bg="#246587", fg="#ffffff").grid(row=0,
                                                                                                                 column=1)
        self.userincorrectText = tk.Label(self, text="Invalid User", width=20, pady=5, font=TEXT1, bg="#195373",
                                 fg="#ff0000")  # Just creates the object, doesn't place it in grid yet.

        self.passincorrectText = tk.Label(self, text="Invalid Pass", width=20, pady=5, font=TEXT1, bg="#195373",
                                      fg="#ff0000")
        username = tk.Label(self, text="Username", width=20, pady=15, padx=10, font=TEXT1, bg="#246587",
                            fg="#ffffff").grid(row=2)
        password = tk.Label(self, text="Password", width=20, pady=30, padx=10, font=TEXT1, bg="#246587",
                            fg="#ffffff").grid(row=3)

        "incorrectText.grid(row=1, column=1)"  # This will only be displayed when password is incorrect (go back when working on commands)

        self.userEntry = tk.Entry(self, width=40, fg="#000000")  # Entry box created for username
        self.passEntry = tk.Entry(self, width=40, fg="#000000", show="*")  # Entry box created for password

        permUsername = self.userEntry.get()

        activateLogin = tk.Button(self, text="Login", width=10, font=TEXT1,
                                  command=lambda: self.createSession(self.userEntry.get(),self.passEntry.get(), parent, controller)).grid(row=4,
                                                                                      column=1)  # Shows Session Frame
        activateRegister = tk.Button(self, text="Register", width=10, font=TEXT1,
                                     command=lambda: self.Quit(False, parent, controller)).grid(row=4,
                                                                                          column=0)  # Shows Register Frame

        self.userEntry.grid(row=2, column=1)  # Will be added to the right of the user label
        self.passEntry.grid(row=3, column=1)  # Will be added to the right of the pass label

    def forgetWidgets(self):
        self.userEntry.delete(0, tk.END)  # Deletes all custom widgets
        self.passEntry.delete(0, tk.END)
        self.userincorrectText.place_forget()
        self.passincorrectText.place_forget()


    def Quit(self, mode, *args):
        self.forgetWidgets()
        if mode == False:
            args[1].showFrame(Register) # Shows session screen
        else:
            args[1].showFrame(Session)
            Session(args[0],args[1], args[2])

    def createSession(self, username, password, *args):
        self.forgetWidgets()  # Removes previous widgets to avoid interference
        found = False
        with open(FILE, "r") as database: # Opens in read mode

            reader = csv.DictReader(database) # Opens as dictionary
            for row in reader:
                if row["Username"] == username and row["Password"] == password: # If username and password matches contents in row
                    found = True
                    self.Quit(found, *args, username)
                    break
                elif row["Username"] == username and row["Password"] != password: # Condition if username is equal to but not password
                    self.passincorrectText.place(x=240, y=90)
                    break
                else:
                    continue # Continues looping

            if found == False:
                self.userincorrectText.place(x=240, y=90) # If username doesn't match




class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        registerText = tk.Label(self, text="Register", width=20, pady=50, font=TEXT1, bg="#246587", fg="#ffffff").grid(row=0,column=1)

        self.userinvalidEntry = tk.Label(self, text="User must be greater than 2 characters", width=32, pady=2, font=TEXT1, bg="#195373", fg="#ff0000")

        self.passinvalidEntry = tk.Label(self, text="Pass must be greater than 5 characters", width=32, pady=2,
                                         font=TEXT1, bg="#195373", fg="#ff0000")

        self.alreadyexist = tk.Label(self, text="Account exists", width=20, pady=5, font=TEXT1, bg="#195373",
                                    fg="#ff0000")  # Creates object for possible situation that it already exists
        self.successful = tk.Label(self, text="Creation successful", width=30, pady=5, font=TEXT1, bg="#195373",
                                  fg="#00ff00")  # Another object just used to confirm succession

        username = tk.Label(self, text="Username", width=20, pady=15, padx=10, font=TEXT1, bg="#246587",
                            fg="#ffffff").grid(row=2)  # Creates label for username
        password = tk.Label(self, text="Password", width=20, pady=30, padx=10, font=TEXT1, bg="#246587",
                            fg="#ffffff").grid(row=3)  # Creates label for password

        self.userEntry = tk.Entry(self, width=40, fg="#000000")  # Entry box created for username
        self.passEntry = tk.Entry(self, width=40, fg="#000000", show="*")  # Entry box created for password

        activateRegister = tk.Button(self, text="Register", command=lambda: self.passRequirements(self.userEntry.get(), self.passEntry.get()), width=10, font=TEXT1,).grid(row=4, column=1)
        activateLogin = tk.Button(self, text="Back to login", width=10, font=TEXT1,
                                  command=lambda: self.Quit(parent, controller)).grid(row=4, column=0)

        self.userEntry.grid(row=2, column=1)  # Will be added to the right of the user label
        self.passEntry.grid(row=3, column=1)  # Will be added to the right of the pass label

    def passRequirements(self, username, password): # Takes in parameters from entry boxes
        if len(username)>2 and len(password)>5: # Creates requirements for each box
            self.forgetWidgets()
            self.completeForm(username, password) # Passes values through to main method
        elif len(username)<2 and len(password)>5:
            self.forgetWidgets()
            self.userinvalidEntry.place(x=200, y=90) # Places invalid entry if it doesn't meet conditions
        elif len(username)>2 and len(password)<5:
            self.forgetWidgets()
            self.passinvalidEntry.place(x=200, y=90)
        else:
            self.forgetWidgets()
            self.passinvalidEntry.place(x=230, y=80)
            self.userinvalidEntry.place(x=230, y=110)

    def completeForm(self, username, password):
        valid = self.checkUsername(username) # Passes username into method and returns True or False
        fieldnames = ["Username","Password"] # Used to read/write file as dictionary

        if valid == True:
            print("Already exists") # Will display label later
            self.forgetWidgets()
            self.alreadyexist.place(x=240, y=90)

        else:
            self.forgetWidgets()
            self.successful.place(x=240, y=90, width=200)
            print("Creating account") # Will display label later
            with open(FILE, "a", newline="") as database: # Opens in write mode
                writer = csv.DictWriter(database, fieldnames)
                writer.writerow({"Username": username, "Password": password}) # Creates a new row in db with data.txt

    def checkUsername(self, username):
        found = False

        with open(FILE, "r") as database: # Opens in read mode
            reader = csv.DictReader(database) # Makes database readable

            for row in reader: # Iterates through db
                if row["Username"] == username:
                    found = True
                    break
                else:
                    continue # Continues iteration of db
            return found


    def forgetWidgets(self):
        self.successful.place_forget()
        self.alreadyexist.place_forget()
        self.userinvalidEntry.place_forget()
        self.passinvalidEntry.place_forget()

    def Quit(self, parent, controller):
        self.forgetWidgets()
        self.userEntry.delete(0, tk.END)
        self.passEntry.delete(0, tk.END)

        controller.showFrame(Login)


class Session(tk.Frame):

    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)  # Standard initialisation procedures
        self.userArray=[]
        self.passArray=[]
        self.notesArray=[]

        store = "".join(args)

        print("Store is:", store)

        logOut = tk.Button(self, text="Log out", command=lambda: self.Quit(parent, controller, store), font=TEXT1, bg="#195373",
                           fg="#ffffff").place(x=0, y=570)


        addLabel = tk.Label(self, text="Add account", font=TEXT1, bg="#195373", fg="#ffffff", pady=4).place(x=100,
                                                                                                            y=20)  # Puts label on screen at specific co-ordinate

        self.invalidLabel = tk.Label(self, text="User & Pass must be filled", font=TEXT2, bg="#195373", fg="#ff0000",
                                     pady=4)  # Puts label on screen at specific co-ordinate

        adduserLabel = tk.Label(self, text="Username", font=TEXT1, bg="#195373", fg="#ffffff", width=10).place(x=100,
                                                                                                               y=50)  # Creates user label
        addpassLabel = tk.Label(self, text="Password", font=TEXT1, bg="#195373", fg="#ffffff", width=10).place(x=100,
                                                                                                               y=75)  # Creates pass label
        addnotesLabel = tk.Label(self, text="Extra Notes", font=TEXT1, bg="#195373", fg="#ffffff", width=10).place(
            x=100,
            y=100)  # Creates note label

        self.accuserEntry = tk.Entry(self, width=40, fg="#000000")  # Creates user input box
        self.accpassEntry = tk.Entry(self, width=40, fg="#000000")  # Creates pass input box
        self.accnotesEntry = tk.Entry(self, width=40, fg="#000000")  # Creates notes input box

        self.accuserEntry.place(x=210, y=50)
        self.accpassEntry.place(x=210, y=75)
        self.accnotesEntry.place(x=210, y=100)

        addButton = tk.Button(self, text="Add", font=TEXT1, bg="#00ff00", fg="#ffffff", bd=1,
                              highlightthickness=0,
                              command=lambda: self.addAccount(self.accuserEntry.get(), self.accpassEntry.get(),
                                                              self.accnotesEntry.get())).place(x=412,
                                                                                            y=20)  # On press it uses the class method

        userLabel = tk.Label(self, text="Username", font=TEXT1, bg="#195373", fg="#ffffff", pady=4, width=10).place(
            x=50,
            y=170)  # Displays user label for accounts
        passLabel = tk.Label(self, text="Password", font=TEXT1, bg="#195373", fg="#ffffff", pady=4, width=10).place(
            x=160, y=170)  # Displays pass label for accounts
        notesLabel = tk.Label(self, text="Notes", font=TEXT1, bg="#195373", fg="#ffffff", pady=4, width=20).place(x=270,
                                                                                                                  y=170)  # Displays notes label for accounts

        self.userBox = tk.Listbox(self, width=17, bg="#1f6d99",
                                  fg="#ffffff", height=17)  # Creates a "box" which contains a list of items
        self.passBox = tk.Listbox(self, width=17, bg="#1f6d99",
                                  fg="#ffffff", height=17)  # Creates a "box" which contains a list of items
        self.notesBox = tk.Listbox(self, width=33, bg="#1f6d99",
                                   fg="#ffffff", height=17)  # Creates a "box" which contains a list of items

        scroller = tk.Scrollbar(self, orient="vertical",
                                command=self.scrollFunc)  # Used to scroll the Y axis of userbox
        scroller.place(x=32, y=200, height=276)

        self.userBox.place(x=52, y=200)
        self.userBox.config(yscrollcommand=scroller.set)  # Scroll command set to scrollbar

        self.passBox.place(x=162, y=200)
        self.notesBox.place(x=270, y=200)

    def scrollFunc(self, *args):  # Method used to scroll through all the boxes, takes multiple arguments
        self.userBox.yview(*args)
        self.passBox.yview(*args)
        self.notesBox.yview(*args)

    def addAccount(self, username, password, notes):
        if len(username) and len(password) > 0:

            self.invalidLabel.place_forget()

            self.userBox.insert(tk.END, username)  # Adds the username value to the end
            self.passBox.insert(tk.END, password)  # Adds the password value to the end
            self.notesBox.insert(tk.END, notes)  # Adds the notes value to the end

            self.userArray.append(username) # Temporarily appends to array
            self.passArray.append(password)
            self.notesArray.append(notes)

            self.accuserEntry.delete(0, tk.END)  # Deletes entire contents of user entry box
            self.accpassEntry.delete(0, tk.END)  # Deletes entire contents of pass entry box
            self.accnotesEntry.delete(0, tk.END)  # Deletes entire contents of notes entry box

        else:
            self.invalidLabel.place(x=210, y=20)

        accRecord = self.userBox.get(0, tk.END)  # Used to generate a list

    def Quit(self, parent, controller, username):
        user1 = username
        print("User", user1)

        tempfile = NamedTemporaryFile(mode="w", delete=False)
        self.accuserEntry.delete(0, tk.END)  # Deletes entire contents of user entry box
        self.accpassEntry.delete(0, tk.END)  # Deletes entire contents of pass entry box
        self.accnotesEntry.delete(0, tk.END)

        self.userBox.delete(0, tk.END)  # Deletes content in all boxes
        self.passBox.delete(0, tk.END)
        self.notesBox.delete(0, tk.END)


        with open(FILE, "r") as database,tempfile:
            fieldnames = ["Username","Password","accountUser","accountPass","accountNotes"]
            reader = csv.DictReader(database, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            print(self.userArray)
            for row in reader:
                print("Test", username)
                if row["Username"] == username:
                    print("Pass")
                    row["accountUser"], row["accountPass"], row["accountNotes"] = self.userArray, self.passArray, self.notesArray
                row = {"Username":row["Username"], "Password": row["Password"],"accountUser": row["accountUser"],"accountPass": row["accountPass"], "accountNotes": row["accountNotes"]}
                # row = {"accountUser": row["accountUsername"],"accountPass": row["accountPassword"], "accountNotes":row["accountNotes"]}
                writer.writerow(row)

        shutil.move(tempfile.name, FILE)
        self.userArray = []
        self.passArray = []
        self.notesArray = []
        controller.showFrame(Login) # switches screen




manager = PasswordManager()
manager.geometry("600x600")  # Makes the window size this big
manager.title("Non-sketchy Password Manager")
manager.resizable(0, 0)  # 0 just represents false in X and Y direction
manager.mainloop()  # Activates program