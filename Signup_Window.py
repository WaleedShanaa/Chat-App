import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as font


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class signupwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        font.nametofont("TkDefaultFont").configure(size=14)

        self.geometry("400x250")
        self.resizable(False,False)
        self.title("What's Down!")
        self.frame = ttk.Frame(
            self,
            padding=10
        )

        self.frame.grid(row=0, column=0, sticky="NSEW")
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.UserLabel = ttk.Label(self.frame, text="User Name: ", padding=5, font=15)
        self.PasswordLabel = ttk.Label(self.frame, text="Password: ", padding=5, font=15)
        self.PasswordLabelAgain = ttk.Label(self.frame, text="Re-Enter Password: ", padding=5, font=15)
        self.UserEntry = ttk.Entry(self.frame, width=16, font=15)
        self.PasswordEntry = ttk.Entry(self.frame, width=16, show="*", font=15)
        self.PasswordEntryAgain = ttk.Entry(self.frame, width=16, show="*", font=15)
        self.BrowseLabel=ttk.Label(self.frame, text="UpLoad a Photo: ", padding=5, font=15)
        self.BrowseButton=ttk.Button(self.frame, text="Browse", padding=15,command=self.BrowseButtonFunc)
        self.SignUp = ttk.Button(self.frame, text="Sign Up", padding=15)
        self.ExitButton=ttk.Button(self.frame, text="Exit!", padding=15,command=self.destroy)



        self.UserLabel.grid(row=0, column=0)
        self.PasswordLabel.grid(row=1, column=0)
        self.PasswordLabelAgain.grid(row=2, column=0)
        self.UserEntry.grid(row=0, column=1)
        self.PasswordEntry.grid(row=1, column=1)
        self.PasswordEntryAgain.grid(row=2, column=1)
        self.BrowseLabel.grid(row=3, column=0)
        self.BrowseButton.grid(row=3, column=1,sticky="EW")
        self.SignUp.grid(row=4,column=0,sticky="EW")
        self.ExitButton.grid(row=4, column=1,sticky="EW")



    def BrowseButtonFunc(self):
        filepath = filedialog.askopenfilename()



