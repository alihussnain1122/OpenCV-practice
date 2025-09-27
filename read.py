import cv2 as cv

#Image Read
img= cv.imread('Photos/cat.jpg')
cv.imshow('ali', img)
cv.waitKey(0)

#Video Read
capture= cv.VideoCapture(0)
while True:
    isTrue, frame= capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

