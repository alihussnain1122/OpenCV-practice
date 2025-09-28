import cv2 as cv
import numpy as nm

blank= nm.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

#1. Paint the image a certain color
# blank[:]= 0,0,255
# cv.imshow('red', blank)
# blank[1:100, 200:300]= 0,255,0
# cv.imshow('Green', blank)

#2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=0)
# cv.imshow('Rectangle', blank)

#3. Draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=0)
# cv.imshow('Circle', blank)

#4. Put Text on image
cv.putText(blank, 'Hello Ali Hussnain', (0,255), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
# image= cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', image)
cv.waitKey(0)