import cv2
import time
import imutils


vs = cv2.VideoCapture(0)
time.sleep(1)

firstFrame = None
area = 500
while True:
    _, frame = vs.read()
    text = "Normal"
    image = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None:
        firstFrame = blur
        continue
    imageDiff = cv2.absdiff(firstFrame, blur)
    _, thresh = cv2.threshold(imageDiff, 32, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours = cv2.findContours(
        dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    for contour in contours:
        if cv2.contourArea(contour) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion Detected"
    cv2.putText(image, "Status: {}".format(text), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Security Feed", image)
    cv2.imshow("Threshhold", thresh)
    cv2.imshow("Dilated", dilated)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()
