from tkinter import *           
from functools import partial
from controller.logic import validateLogin, Load_sign_up



class Login(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        usernameLabel = Label(self, text="User Login", font=("Arial",16)).place(x=250, y=100)

        usernameLabel = Label(self, text="User Name").place(x=200, y=150)
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username).place(x=300, y=150)  

        passwordLabel = Label(self,text="Password").place(x=200, y=200)
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password, show='*').place(x=300, y=200)  

        login= partial(validateLogin,self, controller, username, password)

        sign_up= partial(Load_sign_up, controller)
        
        loginButton = Button(self, text="Login", command=login).place(x=250, y=250)

        SignUpButton = Button(self, text="Create account", command=sign_up).place(x=300, y=250)

        

        