<<<<<<< HEAD
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

=======
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

>>>>>>> 4d386a48264815b9021cb1d8c02420d570c74d6b
