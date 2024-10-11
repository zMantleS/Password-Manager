import csv
import tkinter as tk

tempArray = []
userArray = []

filepath = "test.csv"
# file handling

# Register


root = tk.Tk()

def activate():
    contents = userentry.get()
    userArray.append(contents)
    print(userArray)
    replace()

def leave():
    with open(filepath, "a", newline="") as database:
        fieldnames = ["accountUser","accountPass","accountNotes"]
        writer = csv.DictWriter(database, fieldnames)
        writer.writerow({"accountUser":userArray})
        root.quit()


def replace():
    with open(filepath, "r") as database:
        fieldnames = ["accountUser","accountPass","accountPass"]
        reader = csv.DictReader(database, fieldnames=fieldnames)
        writer = csv.DictReader(database, fieldnames=fieldnames)
        for row in reader:
            if row["accountUser"] == str(userArray):
                row["accountPass"], row["accountNotes"] = "testing","lolol"
            row = {"accountUser": row["accountUser"], "accountPass": row["accountPass"], "accountNotes": row["accountNotes"]}
            writer.writerow(row)


print(userArray)
userlabel = tk.Label(root, text="Username").grid(row=0, column=0)
userentry = tk.Entry(root)
userentry.grid(row=0, column=1)

save = tk.Button(root, width= 10, text="Save", command=leave).grid(row=1,column=0)



button = tk.Button(root, width=10, text="Enter", command=activate).grid(row=1, column=1)




root.geometry("200x200")
root.mainloop()