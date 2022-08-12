import email
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import db
from tkinter import filedialog, messagebox
from tkinter import *
import uuid

class GUI:
    def registerGUI(master):
        master.title("Register")
        
        window = Toplevel(master)
        
        window.geometry('400x300')

        window.title("Attendance App")

        def onClickRegister(master, firstName,lastName,age,tck, email, phone_number):
            master.withdraw()
            # print("info:", firstName, lastName, age, tck, email, phone_number)
            
            # root = Tk()
            # root.wm_withdraw()
            
            # cv2.imshow("photo", img)
            # cv2.waitKey(0)

            path = "./images"
            
            if lastName != "" and firstName != "" and age != "" and tck != "" and phone_number != "":
                filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
                img = cv2.imread(f'{filename}')
                # status = cv2.imwrite(f'{path}/{firstName+"_"+lastName}.jpg', img)
                photo_uuid = uuid.uuid4()
                status = cv2.imwrite(f'{path}/{photo_uuid}.jpg', img)
                
                if status == True:
                    result = db.create_user(lastName, firstName, age, tck, photo_uuid, email, phone_number)
                    if result == 1:    
                        master.deiconify()
                        messagebox.showinfo("Registered", f'Welcome aboard, {firstName}!')
                    else:
                        messagebox.showerror("An error occured: ", result)
                    # root.destroy()
                else:
                    messagebox.showerror("Error", "Something went wrong while selecting picture!")
                    # root.destroy()
            else:
                messagebox.showerror("Empty information", "Please fill all the requirements.")
                # root.destroy()
            
        def clearFields():
            inputFirstName.delete(0, 'end')
            inputLastName.delete(0, 'end')
            inputAge.delete(0, 'end')
            inputTck.delete(0, 'end')
            inputEmail.delete(0, 'end')
            inputPhone.delete(0, 'end')

        # define widgets
        lblFName = Label(window, text="First Name")
        lblLName = Label(window, text="Last Name")
        lblAge = Label(window, text="Age")
        lblTck = Label(window, text="TCK")
        lblEmail = Label(window, text="Email (optional)")
        lblPhone = Label(window, text="Phone Number")

        inputFirstName = Entry(window,width=10)
        inputLastName = Entry(window,width=10)
        inputAge = Entry(window,width=10)
        inputTck = Entry(window,width=10)
        inputEmail = Entry(window,width=10)
        inputPhone = Entry(window,width=10)
        
        btnRegister = Button(window, text="Choose a picture and register", 
                            command=lambda:onClickRegister(master, inputFirstName.get(),inputLastName.get(),inputAge.get(),inputTck.get(), inputEmail.get(), inputPhone.get()))

        btnClearFields = Button(window, text="Clear All", 
                            command=lambda:clearFields())
        
        # place widgets 
        lblFName.grid(column=0, row=0)
        lblLName.grid(column=0, row=1)
        lblAge.grid(column=0, row=2)
        lblTck.grid(column=0, row=3)
        lblEmail.grid(column=0, row=4)
        lblPhone.grid(column=0, row=5)
        
        inputFirstName.grid(column=1, row=0)
        inputLastName.grid(column=1, row=1)
        inputAge.grid(column=1, row=2)
        inputTck.grid(column=1, row=3)
        inputEmail.grid(column=1, row=4)
        inputPhone.grid(column=1, row=5)
        
        btnRegister.grid(column=0, row=7)
        btnClearFields.grid(column=2, row=7)
        
        window.mainloop()   

    
            
    def deleteUI(master):
        window = Toplevel(master)
        window.geometry('400x300')

        window.title("Attendance App")
        
        employers = db.fetchAllEmployers()
        
        if employers:
            for index, emp in enumerate(employers):
                lblFName = Label(window, text=emp[2])
                lblLName = Label(window, text=emp[1])
                
                lblFName.grid(column=0, row=index)
                lblLName.grid(column=1, row=index)
                
                btnDelete = Button(window, text="Delete", command=lambda:db.deleteEmployerById(emp[0]))
                btnDelete.grid(column=2, row=index)
        else:
            messagebox.showerror("Error","No user found")
    def mainGUI():
        master = Tk()
        master.title("Main")
        master.geometry('300x300')
        
        btnRegisterUI = Button(master, text="Register an employer", command=lambda:GUI.registerGUI(master))
        btnRegisterUI.pack(pady=20)
        
        btnRegisterUI = Button(master, text="Delete an employer", command=lambda:GUI.deleteUI(master))
        btnRegisterUI.pack(pady=20)
        master.mainloop()    
            
                