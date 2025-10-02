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
# cv.imshow('Gray', gray)
# cv.waitKey(0)

#Blur an image
blur= cv.GaussianBlur(resize(image), (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
#cv.waitKey(0)

#Edge Cascade
canny= cv.Canny(resize(image), 125,175)
cv.imshow('Canny Edges', canny)
#cv.waitKey(0)

#Dilating the image
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
#cv.waitKey(0)

#Eroding the image
eroded= cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
cv.waitKey(0)

#cropping the image
# resized= resize(image)
# print(resized.shape)
cropped= resize(image)[50:200, 100:180]
cv.imshow('Crop', cropped)
cv.waitKey(0)