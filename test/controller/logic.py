from controller.crud.user import User
from tkinter import *   
import auth

def validateLogin(self, controller, username, password):
    username = username.get()
    password = password.get()

    hash_password = auth.create_hash_passowrd(password)

    user_data = User.get_user_by_email_password(username, hash_password)
    
    if user_data:
        if username == user_data["email"] and hash_password == user_data["password"]:
            
            controller.show_frame("Profile")
    else:
        Message = Label(self,text="username or password is wrong").place(x=250, y=300)

def Load_sign_up(controller):
    controller.show_frame("Sign_up")     
           

def CreateAccount(controller, username, password):
    username = username.get()
    password = password.get()

    user_data = User.create_user(username, password)

    controller.show_frame("Login")

   
	