import cv2
vs = cv2.VideoCapture(0)
while True:
    _, frame = vs.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vs.release()
cv2.destroyAllWindows()
