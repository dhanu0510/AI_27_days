import cv2
import numpy as np
import imutils

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    resized = imutils.resize(image, width=300)
    cv2.imshow('image', image)
    cv2.imshow('resized', resized)
    cv2.imwrite('cat_resized.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
