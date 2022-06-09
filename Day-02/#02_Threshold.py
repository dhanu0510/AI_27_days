import cv2

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # for thresholding, we need to convert the image to grayscale
    # (the grayscale image is a single channel image)
    _, threshold = cv2.threshold(grayImage, 0, 0, cv2.THRESH_BINARY)
    # if the pixel value is greater than 127, it is set to 255(white), otherwise, it is set to 0 (black)
    
    # cv2.THRESH_BINARY: threshold the image to a binary image
    # cv2.THRESH_BINARY_INV: threshold the image to a binary image with the inverse of the original image
    # cv2.THRESH_TRUNC: threshold the image to a binary image with the original image
    # cv2.THRESH_TOZERO: threshold the image to a binary image with the original image
    # cv2.THRESH_TOZERO_INV: threshold the image to a binary image with the inverse of the original image
    cv2.imshow('image', image)
    cv2.imshow('grayImage', grayImage)
    cv2.imshow('threshold', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
