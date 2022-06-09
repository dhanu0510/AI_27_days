import cv2
import imutils
import numpy as np

kernel = np.ones((5, 5), np.uint8)

inside = cv2.imread("Day-02/Morphological_Operations/j_inside.png")
inside = imutils.resize(inside, width=500)

dilation_3 = cv2.dilate(inside, kernel, iterations=4)
erosion_3 = cv2.erode(inside, kernel, iterations=4)

# opening =  erosion followed by dilation
closing = cv2.erode(dilation_3, kernel, iterations=4)

direct_closing = cv2.morphologyEx(
    inside, cv2.MORPH_CLOSE, kernel, iterations=4)

img = np.concatenate((inside, dilation_3, erosion_3,
                     closing, direct_closing), axis=1)
cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
