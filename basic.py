# Convert image into gray scale
import cv2 as cv
 
image= cv.imread('D:\\MY-DOCS/my pic.jpg')
def resize(image, scale=0.1):
    width= int(image.shape[1]* scale)
    height= int(image.shape[0]* scale)
    dimensions= (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Cat', resize(image))

gray= cv.cvtColor(resize(image), cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)