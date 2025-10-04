import cv2 as cv


image= cv.imread('Photos/my.jpg')
def RescaleFrame(frame, scale=0.2):
    width= int(frame.shape[1]* scale)
    height= int(frame.shape[0]* scale)

    dimensions= (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resize= RescaleFrame(image)
#cv.imshow('Person', RescaleFrame(image))
gray= cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

haar=cv.CascadeClassifier('haar_face.xml')
haar_rect= haar.detectMultiScale(gray,  scaleFactor=1.1, minNeighbors=3)
print(f'No. of faces found= {len(haar_rect)}')

for (x,y,w,h) in haar_rect:
    cv.rectangle(resize,(x,y),(x+w,y+h), (0,255,0),thickness=2)
cv.imshow('Detected face', resize)

cv.waitKey(0)
cv.destroyAllWindows()