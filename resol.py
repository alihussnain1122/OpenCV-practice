import cv2 as cv


capture= cv.VideoCapture(0)
#resolution change
def ChangeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

ChangeRes(640, 480)
while True:
    isTrue, frame= capture.read()

    cv.imshow('Resized Webcam', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()