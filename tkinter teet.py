import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class App(tk.Tk): # This is just used to add pages

    def __init__(self, *args, **kwargs): # Prerequisites
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) # Frame is just a window
        # Pack for simple windows, grid for complex windows
        container.pack(side="top", fill="both", expand = True) # Fill fills in space you've allocated, fill basically extends limits

        container.grid_rowconfigure(0, weight=1) # 0 is minimum size, weight is just priority (1 is the same for both)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # Changes different screens/different types of windows

        for f in (StartPage, PageOne, PageTwo): # Constantly loops to add new frame
            frame = f(container, self)
            self.frames[f] = frame # Saves F to dictionary so it can be shown
            frame.grid(row=0, column=0,
                       sticky="nsew")  # Grid, row and column doesn't matter but act like "priority", sticky can put everything NESW, stretches everythign to size of window, not just NORTH to SOUTH

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # tkraise just raises it to the front, basically hides the page before it like another window

def qf(string):
    print(string)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # parent is just the class above
        label = tk.Label(self, text="Hello!", font=LARGE_FONT) # created an object, initialises it
        label.pack(pady=10,padx=10) # basically "padding" size from top and sides

        button1= tk.Button(self, text="Visit page 1",
                           command=lambda: controller.show_frame(PageOne)) # lamda is a throw away function allows parameters to be passed through
        button1.pack()

        button2 = tk.Button(self, text="Visit page 2",
                            command=lambda: controller.show_frame(
                                PageTwo))  # lamda is a throw away function allows parameters to be passed through
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)  # parent is just the class above
        label = tk.Label(self, text="Hello!", font=LARGE_FONT)  # created an object, initialises it
        label.pack(pady=10, padx=10)  # basically "padding" size from top and sides

        button1 = tk.Button(self, text="Visit page two",
                            command=lambda: controller.show_frame(
                                PageTwo))  # lamda is a throw away function allows parameters to be passed through
        button1.pack()

        button2 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(
                                StartPage))  # lamda is a throw away function allows parameters to be passed through
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)  # parent is just the class above
        label = tk.Label(self, text="Hello!", font=LARGE_FONT)  # created an object, initialises it
        label.pack(pady=10, padx=10)  # basically "padding" size from top and sides

        button1 = tk.Button(self, text="Visit page one",
                            command=lambda: controller.show_frame(
                                PageOne))  # lamda is a throw away function allows parameters to be passed through
        button1.pack()

        button2 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(
                                StartPage))  # lamda is a throw away function allows parameters to be passed through
        button2.pack()


app = App()
app.geometry("500x500")
app.title("Password Manager")
app.mainloop()