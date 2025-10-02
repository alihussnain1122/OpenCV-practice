import cv2 as cv
import numpy as np

image= cv.imread('Photos/cat.jpg')

def translate(image, x, y):
    transMat= np.float32([[1,0,x], [0,1,y]])
    dimensions= (image.shape[1],  image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

# x= right, y= down
# -x= left, -y= up
translated= translate(image, -100, -100)
cv.imshow('Translated', translated)
#cv.waitKey(0)

#Rotation
def rotate(image, angle, rotPoint=None):
    (height, width)= image.shape[:2]
    if rotPoint is None:
        rotPoint= (width//2, height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (width, height)

    return cv.warpAffine(image, rotMat, dimensions)
    
rotated= rotate(image, -45)
cv.imshow('Rotated', rotated)

rotated_rotate= rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotate)
cv.waitKey(0)    