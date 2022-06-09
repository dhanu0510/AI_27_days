import cv2

image = cv2.imread('cat.png')
if image is None:
    print('Image not found')
    exit()
else:
    cv2.rectangle(image, (2000, 1000), (3500, 2000), (0, 255, 0), 10)
    cv2.putText(image, 'Cat', (2000, 1000),
                cv2.FONT_HERSHEY_SIMPLEX, 8, (0, 255, 0), 20)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
