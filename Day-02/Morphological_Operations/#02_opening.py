import cv2
import imutils
import numpy as np

kernel = np.ones((5, 5), np.uint8)

outside = cv2.imread("Day-02/Morphological_Operations/j_outside.png")
outside = imutils.resize(outside, width=500)

erosion_3 = cv2.erode(outside, kernel, iterations=3)
dilation_3 = cv2.dilate(outside, kernel, iterations=3)

# opening =  erosion followed by dilation
opening = cv2.dilate(erosion_3, kernel, iterations=3)

direct_opening = cv2.morphologyEx(
    outside, cv2.MORPH_OPEN, kernel, iterations=3)

img = np.concatenate((outside, erosion_3, dilation_3,
                     opening, direct_opening), axis=1)
cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
