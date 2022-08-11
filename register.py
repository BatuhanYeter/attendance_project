import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import db
from tkinter import filedialog
from tkinter import *


print("Enter your first name:")
firstName = input()
print("Enter your lastname:")
lastName = input()
print("Enter your age:")
age = input()

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

img = cv2.imread(f'{root.filename}')
cv2.imshow("photo", img)
cv2.waitKey(0)

path = "./images"
 
status = cv2.imwrite(f'{path}/{firstName+"_"+lastName}.jpg', img)

if status == True:
    db.create_user(lastName=lastName, firstName=firstName, age=age)
    print("welcome to the team")


