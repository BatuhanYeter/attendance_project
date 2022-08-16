import email
from msilib.schema import ComboBox
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import db
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter import ttk
import project
import uuid

class GUI:
    def registerGUI(master):
        master.title("Register")
        
        window = Toplevel(master)
        
        window.geometry('400x300')

        window.title("Attendance App")

        def onClickRegister(master, firstName,lastName,age,tck, email, phone_number, address):
            master.withdraw()
            # print("info:", firstName, lastName, age, tck, email, phone_number)
            
            # root = Tk()
            # root.wm_withdraw()
            
            # cv2.imshow("photo", img)
            # cv2.waitKey(0)

            path = "./images"
            
            address_id = db.getAddressIdByName(address)
            
            if lastName != "" and firstName != "" and age != "" and tck != "" and phone_number != "" and address_id != "":
                filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
                img = cv2.imread(f'{filename}')
                # status = cv2.imwrite(f'{path}/{firstName+"_"+lastName}.jpg', img)
                photo_uuid = uuid.uuid4()
                status = cv2.imwrite(f'{path}/{photo_uuid}.jpg', img)
                
                print("address id: ", address_id)
                if status == True:
                    result = db.create_user(lastName, firstName, age, tck, photo_uuid, email, phone_number, address_id)
                    if result == 1:    
                        master.deiconify()
                        messagebox.showinfo("Registered", f'Welcome aboard, {firstName}!')
                    else:
                        os.remove(f'{path}/{photo_uuid}.jpg')
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
        
        # label
        Label(window, text = "Select Address :",
                font = ("Times New Roman", 10)).grid(column = 0,
                row = 7, padx = 10, pady = 25)
        
        # Combobox creation
        n = StringVar()
        address_chosen = ttk.Combobox(window, width = 27, textvariable = n)

        data = db.getAddresses()
        address_choices = []
        for id, address in data:
            address_choices.append(address)
            print(id, address)

        # Adding combobox drop down list
        address_chosen['values'] = address_choices
        
        address_chosen.grid(column = 1, row = 7)
        address_chosen.current()
        
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
                            command=lambda:onClickRegister(master, 
                                                           inputFirstName.get(),
                                                           inputLastName.get(),
                                                           inputAge.get(),
                                                           inputTck.get(), inputEmail.get(), 
                                                           inputPhone.get(), address_chosen.get()))

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
        
        btnRegister.grid(column=0, row=8)
        btnClearFields.grid(column=2, row=8)
        
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
                
                btnDelete = Button(window, text="Delete", command=lambda:[deleteAndUpdateUI(emp[0])])
                btnDelete.grid(column=2, row=index)
        else:
            messagebox.showerror("Error","No user found")

        def deleteAndUpdateUI(id):
            res = db.deleteEmployerById(id)
            if(res == 1):
                messagebox.showinfo("Info", "Employer deleted!")
                window.destroy()
                window.mainloop()
            else:
                messagebox.showerror(f'Error", "Something went wrong: {res}')
    
    def extractToCsvUI(master):
        window = Toplevel(master)
        window.geometry('400x300')

        window.title("Attendance App")
        def onClickCsv(id):
            attendance_data = db.fetchAttendanceById(id)
            db.saveAsCsv(attendance_data)
            messagebox.showinfo("Info", "Attendance report created.")
        # label
        Label(window, text = "Enter id: ",
                font = ("Times New Roman", 10)).grid(column = 0,
                row = 2, padx = 10, pady = 25)
        inputId = Entry(window, width=15)
        inputId.grid(column=1, row=2)
        Button(window, text="Extract Report", command=lambda:onClickCsv(inputId.get())).grid(column=2, row=2)
        
        
            
    def startSystem():
        project.startSystem()
    
    def mainGUI():
        master = Tk()
        master.title("Main")
        master.geometry('300x300')
        
        btnRegisterUI = Button(master, text="Register an employer", command=lambda:GUI.registerGUI(master))
        btnRegisterUI.pack(pady=20)
        
        deleteEmployerUI = Button(master, text="Delete an employer", command=lambda:GUI.deleteUI(master))
        deleteEmployerUI.pack(pady=20)
        
        recognitionSystemUI = Button(master, text="Start Recognition System", command=lambda:GUI.startSystem())
        recognitionSystemUI.pack(pady=20)
        
        extractCsvUI = Button(master, text="Extract Attendance Report", command=lambda:GUI.extractToCsvUI(master))
        extractCsvUI.pack(pady=20)
        
        master.mainloop()    
            
                