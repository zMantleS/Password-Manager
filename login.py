import csv
filepath = "E:\computing project\database.csv"

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
