import cv2
import face_recognition

imgMe = cv2.imread("me_1.jpg")
rgb_me = cv2.cvtColor(imgMe, cv2.COLOR_BGR2RGB)
face_location_me = face_recognition.face_locations(rgb_me)[0]
encoding_me = face_recognition.face_encodings(rgb_me)[0]
cv2.rectangle(
    imgMe, (face_location_me[3], face_location_me[0]),
    (face_location_me[1], face_location_me[2]), (255, 0, 255), 2)

imgElon = cv2.imread("./images/elon.jpg")
rgb_elon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
face_location = face_recognition.face_locations(rgb_elon)[0]
encoding_elon = face_recognition.face_encodings(rgb_elon)[0]
cv2.rectangle(
    imgElon, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (255, 0, 255), 2)


imgTest = cv2.imread("./images/hugh_jackman.jpg")
rgb_test = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
face_location_test = face_recognition.face_locations(rgb_test)[0]
encoding_test = face_recognition.face_encodings(rgb_test)[0]
cv2.rectangle(
    imgTest, (face_location_test[3], face_location_test[0]), (face_location_test[1], face_location_test[2]), (255, 0, 255), 2)

imgJared = cv2.imread("./images/jared.jpg")
rgb_jared = cv2.cvtColor(imgJared, cv2.COLOR_BGR2RGB)
face_location_jared = face_recognition.face_locations(rgb_jared)[0]
encoding_jared = face_recognition.face_encodings(rgb_jared)[0]
cv2.rectangle(
    imgJared, (face_location_jared[3], face_location_jared[0]),
    (face_location_jared[1], face_location_jared[2]), (255, 0, 255), 2)

# result = face_recognition.compare_faces([encoding_jared], encoding_test)
# face_distance = face_recognition.face_distance([encoding_jared], encoding_test)
# print("Result for jared and test (me): ", result, "Distance: ", face_distance)

result = face_recognition.compare_faces([encoding_me], encoding_test)
face_distance = face_recognition.face_distance([encoding_me], encoding_test)
print("Result for me and test: ", result, "Distance: ", face_distance)

cv2.putText(imgTest, f'{result} {round(face_distance[0], 2)}', (
    50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# Resize images
imgMe = cv2.resize(imgMe, (1280, 800))
imgTest = cv2.resize(imgTest, (1280, 800))

cv2.imshow("Test", imgTest)
cv2.imshow("Me", imgMe)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)

#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# -------------------------------

# test_images = ["elon", "hugh_jackman", "jared", "kobe", "me_2"]

# main_img = cv2.imread("me_1.jpg")
# main_rgb_img = cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB)
# main_img_encoding = face_recognition.face_encodings(main_rgb_img)[0]

# for img in test_images:
#     test_image = cv2.imread("./images/" + img + ".jpg")
#     rgb_img = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
#     img_encoding = face_recognition.face_encodings(rgb_img)[0]

#     result = face_recognition.compare_faces([main_img_encoding], img_encoding)

#     print("Result for {}:".format(img), result)


# cv2.imshow("Img", main_img)
# # cv2.imshow("Img", img_elon)
# cv2.waitKey(0)
