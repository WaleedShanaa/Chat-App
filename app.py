import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from chat import Chat
from Signup_Window import signupwindow




try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"

username=""



class LoginScreen(tk.Tk):
    istr=False




    def __init__(self):
        super().__init__()
        self.iconbitmap('icon.ico')
        font.nametofont("TkDefaultFont").configure(size=14)
        self.username=""
        #Take Users to the data base
        self.Users = {"WaleedShanaa": "123456789",
                      "AliNazm": "123456789",
                      "GamzeKrc": "123456789",
                      "EsenTekkanat": "123456789",
                      "EmreTanker": "123456789",
                      "PhoebeShanaa": "123456789",
                      }
        self.geometry("400x300")
        self.resizable(False,False)
        self.title("What's Down!")
        self.frame = ttk.Frame(
            self,
            style="Messages.TFrame",
            padding=10
        )
        self.frame.grid(row=0, column=0, sticky="NSEW")





        self.UserLabel = ttk.Label(self.frame, text="User Name: ",padding=5)
        self.PasswordLabel = ttk.Label(self.frame, text="Password: ",padding=5)
        self.UserEntry = ttk.Entry(self.frame, width=16,font=15)
        self.PasswordEntry = ttk.Entry(self.frame, width=16,show="*",font=15)
        self.Or = ttk.Label(self.frame, text="Or: ",padding=5)
        self.SignUp=ttk.Button(self.frame,text="Sign Up!",padding=15,command=self.SignUp)
        self.SignIn = ttk.Button(self.frame, text="Sign In",padding=15,command=self.LogInCommand)
        self.Exit = ttk.Button(self.frame, text="Exit!",padding=15,command=self.destroy)


        self.UserLabel.grid(row=0, column=0)
        self.PasswordLabel.grid(row=1, column=0)
        self.UserEntry.grid(row=0, column=1)
        self.PasswordEntry.grid(row=1, column=1)
        self.PasswordEntry.grid(row=1, column=1)
        self.SignIn.grid(row=2, column=0)
        self.Exit.grid(row=2, column=1)
        self.Or.grid(row=3, column=0, columnspan=2)
        self.SignUp.grid(row=4, column=0,columnspan=2)


        #self.frame.bind("<Return>",self.LogInCommand)
        #self.frame.bind("<KP_Enter>", self.LogInCommand)





        self.mainloop()

    def SignUp(self):
        rootSignup=signupwindow()
        rootSignup.mainloop()

    def LogInCommand(self):
        UserGet = self.UserEntry.get()
        PassGet = self.PasswordEntry.get()
        dic = {UserGet: PassGet}
        for userpass in dic:
            for element in self.Users:
                if userpass == element and dic[userpass] == self.Users[userpass]:
                    LoginScreen.istr = True
                    global username
                    username=UserGet
                    self.destroy()








class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('icon.ico')

        self.title("What's Down")
        self.geometry("1200x500")
        self.minsize(800, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(
            self,
            background=COLOUR_LIGHT_BACKGROUND_3,
            style="Messages.TFrame",
            un=username
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")
        font.nametofont("TkDefaultFont").configure(size=14)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)

        style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)

        style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
        style.map(
            "SendButton.TButton",
            background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
        )

        style.configure(
            "FetchButton.TButton", background=COLOUR_LIGHT_BACKGROUND_1, borderwidth=0
        )

        style.configure(
            "Time.TLabel",
            padding=5,
            background=COLOUR_LIGHT_BACKGROUND_1,
            foreground=COLOUR_LIGHT_TEXT,
            font=8
        )

        style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
        style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)







root1=LoginScreen()
if LoginScreen.istr:

    root=Messenger()
    root.mainloop()


