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


Register = Register("tes", "passord412")
Register.register()
