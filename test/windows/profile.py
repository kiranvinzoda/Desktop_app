from tkinter import *             


class Profile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        usernameLabel = Label(self, text="user profile").place(x=200, y=150)




