from tkinter import *             
from functools import partial
from controller.logic import CreateAccount

class Sign_up(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        usernameLabel = Label(self, text="Craete Account", font=("Arial",16)).place(x=250, y=100)

        usernameLabel = Label(self, text="User Name").place(x=200, y=150)
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username).place(x=300, y=150)  

        passwordLabel = Label(self,text="Password").place(x=200, y=200)
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password, show='*').place(x=300, y=200)  

        create= partial(CreateAccount, controller, username, password)
        
        loginButton = Button(self, text="Sign Up", command=create).place(x=300, y=250)
 