import time
import face_recognition
import numpy as np
import ctypes
import uuid, os
from PyQt5 import QtCore, QtGui, QtWidgets
import db
from PyQt5.QtCore import pyqtSlot
from tkinter import filedialog, messagebox
import cv2
import sys

class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.resize(262, 349)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 230, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 71, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        data = db.getAddresses()
        address_choices = []
        for id, address in data:
            address_choices.append(address)
            
        self.comboBox.addItems(address_choices)    
        self.pushButton.clicked.connect(self.onClickRegister)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Register"))
        self.label.setText(_translate("mainWindow", "First Name"))
        self.label_2.setText(_translate("mainWindow", "Last Name"))
        self.label_3.setText(_translate("mainWindow", "Age"))
        self.label_4.setText(_translate("mainWindow", "TCK"))
        self.label_5.setText(_translate("mainWindow", "Email"))
        self.label_6.setText(_translate("mainWindow", "Phone Number"))
        self.label_7.setText(_translate("mainWindow", "Address"))
        self.pushButton.setText(_translate("mainWindow", "Choose a Picture and Register"))

    def onClickRegister(self):
        self.firstName = self.lineEdit.text() 
        self.lastname = self.lineEdit_2.text()
        self.age = self.lineEdit_3.text()
        self.tck = self.lineEdit_4.text()
        self.email = self.lineEdit_5.text()
        self.phone_number = self.lineEdit_6.text()
        self.address = self.comboBox.currentText()
        
        path = "./media/images"
        address_id = db.getAddressIdByName(self.address)
        if self.lastname != "" and self.firstName != "" and self.age != "" and self.tck != "" and self.phone_number != "" and address_id != "":
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            img = cv2.imread(f'{filename}')
            # status = cv2.imwrite(f'{path}/{firstName+"_"+lastName}.jpg', img)
            photo_uuid = uuid.uuid4()
            
            # resize
            scale_percent = 30 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            print(f"new width n height: {width}, {height}")
            dim = (width, height)
            
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            status = cv2.imwrite(f'{path}/{photo_uuid}.jpg', resized)
            
            print("address id: ", address_id)
            if status == True:
                result = db.create_user(self.lastname, self.firstName, self.age, self.tck, photo_uuid, self.email, self.phone_number, address_id)
                if result == 1:    
                    messagebox.showinfo("Registered", f'Welcome aboard, {self.firstName}!')
                else:
                    os.remove(f'{path}/{photo_uuid}.jpg')
                    messagebox.showerror("An error occured: ", result)
                # root.destroy()
            else:
                messagebox.showerror("Error", "Something went wrong while selecting picture!")
                # root.destroy()
        else:
            messagebox.showerror("Empty information", "Please fill all the requirements.")

class DeleteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.resize(262, 349)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        
        
        self.pushButton.clicked.connect(self.onClickDelete)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Delete"))
        self.label.setText(_translate("mainWindow", "Enter ID: "))
        self.pushButton.setText(_translate("mainWindow", "Delete"))
    
    def onClickDelete(self):
        self.worker_id_del = self.lineEdit.text()
        if self.worker_id_del != "":
            result = db.deleteWorkerById(self.worker_id_del)
            if result == 1:    
                messagebox.showinfo("Deleted", f'Deleted: {self.worker_id_del}!')
            else:
                messagebox.showerror("Error", f"Something went wrong: {result}")
        else:
            messagebox.showerror("Empty information", "Please enter an id.")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.labelFullName = QtWidgets.QLabel(self)
        self.labelFullName.setGeometry(QtCore.QRect(40, 300, 121, 31))
        self.labelFullName.setObjectName("labelFullName")
        self.labelAge = QtWidgets.QLabel(self)
        self.labelAge.setGeometry(QtCore.QRect(40, 330, 121, 31))
        self.labelAge.setObjectName("labelAge")
        self.labelTCK = QtWidgets.QLabel(self)
        self.labelTCK.setGeometry(QtCore.QRect(40, 360, 121, 31))
        self.labelTCK.setObjectName("labelTCK")
        self.labelPhone = QtWidgets.QLabel(self)
        self.labelPhone.setGeometry(QtCore.QRect(40, 390, 121, 31))
        self.labelPhone.setObjectName("labelPhone")
        self.label_image = QtWidgets.QLabel(self)
        self.label_image.setGeometry(QtCore.QRect(30, 30, 191, 161))
        self.label_image.setObjectName("label_image")
        
        self.setObjectName("MainWindow")
        self.resize(705, 494)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(500, 30, 75, 23))
        self.btnRegister.setObjectName("btnRegister")
        
        
        
        self.btnStartSystem = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartSystem.setGeometry(QtCore.QRect(500, 120, 75, 23))
        self.btnStartSystem.setObjectName("btnStartSystem")
        
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(500, 60, 75, 23))
        self.btnDelete.setObjectName("btnDelete")
        
        self.btnCsvExtract = QtWidgets.QPushButton(self.centralwidget)
        self.btnCsvExtract.setGeometry(QtCore.QRect(500, 90, 75, 23))
        self.btnCsvExtract.setObjectName("btnCsvExtract")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(260, 190, 118, 23))
        self.progressBar.hide()
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.btnRegister.clicked.connect(self.openRegisterWindow)
        self.btnStartSystem.clicked.connect(self.startSystem)
        self.btnDelete.clicked.connect(self.openDeleteWindow)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.btnStartSystem.setText(_translate("MainWindow", "Start System"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnCsvExtract.setText(_translate("MainWindow", "Extract Csv"))

    def openRegisterWindow(self, checked):
        self.w = RegisterWindow()
        self.w.show()

    def openDeleteWindow(self, checked):
        self.w = DeleteWindow()
        self.w.show()
       
    def statusBar(self):
        self.progressBar.show()
        # setting for loop to set value of progress bar
        for i in range(101):
            # slowing down the loop
            time.sleep(0.05)
  
            # setting value to progress bar
            self.progressBar.setValue(i)
        self.progressBar.hide()

    def startSystem(self):
        path = "./media/images"        
        
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)

        # cls = class
        for cls in myList:
            current_img = cv2.imread(f'{path}/{cls}')
            images.append(current_img)
            classNames.append(os.path.splitext(cls)[0])
        print(classNames)


        def findEncodings(images):
            encodeList = []
            for img in images:
                rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encoding = face_recognition.face_encodings(rgb)[0]
                encodeList.append(encoding)
            return encodeList

        self.statusBar()
        
        encodeListKnown = findEncodings(images)
        print("Encoding completed. Number of images encoded: ", len(encodeListKnown))

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            rgb = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

            face_current_location_frame = face_recognition.face_locations(rgb)
            encoding_current_frame = face_recognition.face_encodings(
                rgb, face_current_location_frame)

            for encodedFace, faceLocation in zip(encoding_current_frame, face_current_location_frame):
                matches = face_recognition.compare_faces(encodeListKnown, encodedFace)
                face_distance = face_recognition.face_distance(
                    encodeListKnown, encodedFace)
                # print(face_distance)
                matchIndex = np.argmin(face_distance)

                if matches[matchIndex]:
                    photo_uuid = classNames[matchIndex]
                    # print(name)
                    y1, x1, y2, x2 = faceLocation
                    y1, x1, y2, x2 = y1*4, x1*4, y2*4, x2*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                    
                    # cv2.putText(img, photo_uuid, (x1+6, y2-6),
                    #             cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    
                    # fetch employer data
                    worker = db.fetchWorkerByPhotoId(photo_uuid)
                    print(worker)
                    # save the worker's entrance
                    db.save_entrance(worker[0])

                    # show info --.jpg
                    self.pixmap = QtGui.QPixmap(f'media/{worker[5]}')
                    # self.pixmap_resize = self.pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
                    self.pixmap_resize = self.pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                    
                    self.label_image.setPixmap(self.pixmap)
                    self.label_image.resize(self.pixmap_resize.width(),
                          self.pixmap_resize.height())
                    
                    self.labelFullName.setText(f"Worker: {worker[2]} {worker[1]}")
                    self.labelAge.setText(f"Age: {worker[3]}")
                    self.labelTCK.setText(f"TCK: {worker[4]}")
                    self.labelPhone.setText(f"Phone Number: {worker[7]}")
                    
                    # TODO: Send signal and open the gate
                    
            cv2.imshow("Webcam", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
                break
        

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    app.exec_()