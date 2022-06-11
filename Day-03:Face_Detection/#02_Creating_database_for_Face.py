import cv2
import os
alg = "Day-03:Face_Detection/haarcascade_frontalface_default.xml"
dataset = "Day-03:Face_Detection/dataset"
name = input("Enter your name: ")
countt = int(input("How many images do you want: "))

path = os.path.join(dataset, name)

if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130, 100)

# convert xml to algo
haar_cascade = cv2.CascadeClassifier(alg)

cap = cv2.VideoCapture(0)

count = 0
while count < countt:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        faceOnly = gray[y:y + h, x:x + w]
        faceOnly = cv2.resize(faceOnly, (width, height))
        cv2.imwrite(os.path.join(path, name + str(count) + ".jpg"), faceOnly)
        count += 1

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
