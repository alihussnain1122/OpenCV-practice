import cv2 as cv
import numpy as np
image= cv.imread('Photos/cat.jpg')
#split color channels of image
b,g,r= cv.split(image)
cv.imshow('image',image)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

blank= np.zeros(image.shape[:2], dtype='uint8')
blue=cv.merge([b,blank,blank])
green= cv.merge([blank, g, blank])
red= cv.merge([blank, blank, r])
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

#check shape of image and b,g,r channels
print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)
#merge color channels
merged= cv.merge([b,g,r])
cv.imshow("merged image", merged)

cv.waitKey(0)