import cv2

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    # (21,21) is the size of kernel, which is generally odd number
    gaussian = cv2.GaussianBlur(image, (21, 21), 0)
    cv2.imshow('image', image)
    cv2.imshow('gaussian', gaussian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
