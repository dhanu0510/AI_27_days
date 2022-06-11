import cv2
import imutils
import numpy as np


cap = cv2.VideoCapture(0)
_, frame1 = cap.read()
_, frame2 = cap.read()
frame1 = imutils.resize(frame1, width=500)
frame2 = imutils.resize(frame2, width=500)


while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    # merged = np.concatenate((frame, gray), axis=0)
    cv2.imshow("frame", frame1)
    cv2.imshow("gray", gray)
    cv2.imshow("thresh", thresh)
    cv2.imshow("diff", diff)
    cv2.imshow("dilated", dilated)
    frame1 = frame2
    _, frame2 = cap.read()
    frame2 = imutils.resize(frame2, width=500)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
