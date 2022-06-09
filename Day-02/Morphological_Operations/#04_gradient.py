import cv2
import imutils
import numpy as np

kernel = np.ones((5, 5), np.uint8)

image = cv2.imread("Day-02/Morphological_Operations/j.png")
image = imutils.resize(image, width=500)

dilated = cv2.dilate(image, kernel, iterations=3)
eroded = cv2.erode(image, kernel, iterations=3)

diff = cv2.absdiff(dilated, eroded)

gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("image", image)
cv2.imshow("Gradient", gradient)
cv2.imshow("Diff", diff)


cv2.waitKey(0)
cv2.destroyAllWindows()
