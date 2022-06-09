import cv2
import numpy as np

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image", image)
    cv2.imshow('grayImage', grayImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
