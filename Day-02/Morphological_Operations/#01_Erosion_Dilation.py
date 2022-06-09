import cv2
import imutils
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("Day-02/Morphological_Operations/j.png")
img = imutils.resize(img, width=500)
erosion_1 = cv2.erode(img, kernel, iterations=1)
erosion_3 = cv2.erode(img, kernel, iterations=3)

erosion = np.concatenate((img, erosion_1, erosion_3), axis=1)

dilation_1 = cv2.dilate(img, kernel, iterations=1)
dilation_3 = cv2.dilate(img, kernel, iterations=3)

dilation = np.concatenate((img, dilation_1, dilation_3), axis=1)


# cv2.imshow("Original", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
