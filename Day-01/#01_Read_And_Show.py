import cv2
import numpy as np

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
