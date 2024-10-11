# ALL PROJECT GOES HERE 

import csv
filepath = "E:\computing project\database.csv"

class Register():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        checkUsername = Register.checkUsername(self.username)
        fieldnames = ["Username","Password"]

        if checkUsername == True:
            print("Account already exists")
        else:
            with open(filepath, "a", newline="") as database:
                writer = csv.DictWriter(database, fieldnames)
                writer.writerow({"Username":self.username, "Password": self.password})


    def checkUsername(self, username):
        found = False

        with open(filepath, "r") as database:
            reader = csv.DictReader(database)

            for row in reader:
                if (row["Username"] == self.username):
                    found = True
                    return found
                    break
                else:
                    continue

        return found


class Login():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        rowID = 1
        fieldnames = ["Username","Password"]
        checkUsername = Register.checkUsername(self.username)

        if checkUsername == False:
            print("USername doesn't exist")

        else:
            with open(filepath, "r") as database:
                reader = csv.DictReader(database)
                for row in reader:
                    if (row["Username"] == self.username) and (row["Password"] == self.password):
                        print("Login successful")
                        break
                    else:
                        continue
                print("Incorrect password")


Log = Login("tes", "passord412")

Log.login()

