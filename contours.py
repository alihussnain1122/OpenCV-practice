import cv2 as cv
import numpy as np

image= cv.imread('Photos/cat.jpg')
cv.imshow('Cats', image)

gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
blur= cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur) 
canny= cv.Canny(image, 125,175)
cv.imshow('Canny', canny)

contours, hierarchies= cv.findContours(canny,  cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(image, contours, -1, (0,255,0))
cv.imshow('Contours', image)

cv.waitKey(0)