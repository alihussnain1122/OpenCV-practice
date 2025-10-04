import cv2 as cv

image= cv.imread('Photos/cat.jpg')
cv.imshow("cat", image)

# BGR to HSV
hsv= cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
# BGR to Gray
gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#BGR to LAB
lab= cv.cvtColor(image, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

cv.waitKey(0)