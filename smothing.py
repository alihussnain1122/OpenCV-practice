import cv2 as cv

image= cv.imread('Photos/cat.jpg')
cv.imshow('Image',  image)
#averaging 
average= cv.blur(image,(7,7))
cv.imshow('Averaging', average)
#gaussian blur
gauss= cv.GaussianBlur(image,(7,7),0)
cv.imshow('Gaussian Blur', gauss)
#median blur
median= cv.medianBlur(image,7)
cv.imshow('Median Blur', median)
#Bilateral blur
bilateral= cv.bilateralFilter(image, 13, 15,15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)