import cv2
import numpy as np

img = cv2.imread("Day-02/opencv.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 100, 255, 0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print(len(contours))

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
