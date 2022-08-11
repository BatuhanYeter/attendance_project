import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import db
from tkinter import filedialog, messagebox
from tkinter import *

def registerGUI():
    window = Tk()
    window.geometry('400x400')

    window.title("Attendance App")

    lblFName = Label(window, text="First Name")
    lblLName = Label(window, text="Last Name")
    lblAge = Label(window, text="Age")

    inputFirstName = Entry(window,width=10)
    inputLastName = Entry(window,width=10)
    inputAge = Entry(window,width=10)

    btnRegister = Button(window, text="Register and choose a picture", command=lambda:onClickRegister(inputFirstName.get(), inputLastName.get(), inputAge.get()))
    # btnPicture = Button(window, text="Choose a picture", command=lambda:onClickPicture(inputFirstName.get(), inputLastName.get()))

    lblFName.grid(column=0, row=0)
    lblLName.grid(column=0, row=1)
    lblAge.grid(column=0, row=2)

    inputFirstName.grid(column=1, row=0)
    inputLastName.grid(column=1, row=1)
    inputAge.grid(column=1, row=2)
    
    # btnPicture.grid(column=1, row=3)
    btnRegister.grid(column=1, row=4)
    
    window.mainloop()

def onClickRegister(firstName,lastName,age):
    root = Tk()
    root.wm_withdraw()
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    img = cv2.imread(f'{root.filename}')
    # cv2.imshow("photo", img)
    # cv2.waitKey(0)

    path = "./images"
    
    status = cv2.imwrite(f'{path}/{firstName+"_"+lastName}.jpg', img)
    if status == True:
        if lastName != "" and firstName != "" and age != "":
            db.create_user(lastName=lastName, firstName=firstName, age=age)
            messagebox.showinfo("Registered", f'Welcome aboard, {firstName}!')
            root.destroy()
        else:
            messagebox.showerror("Empty information", "Please fill all the requirements.")
            root.destroy()
    else:
        messagebox.showerror("Error", "Something went wrong!")
        root.destroy()

        
registerGUI()