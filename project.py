import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import db

path = "images"

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

# def markAttendance(name):
    with open("attendance.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dtString}')

        now = datetime.now()
        dtString = now.strftime("%H:%M:%S")
        f.writelines(f'\n{name},{dtString}')


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
            name = classNames[matchIndex]
            # print(name)
            y1, x1, y2, x2 = faceLocation
            y1, x1, y2, x2 = y1*4, x1*4, y2*4, x2*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
            # search for the id
            employer_id = db.find_employerId(name)
            # save the worker's entrance
            db.save_entrance(employer_id)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
