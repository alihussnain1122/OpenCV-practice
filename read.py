import cv2 as cv

#Image Read
# img= cv.imread('Photos/cat.jpg')
# cv.imshow('ali', img)
# cv.waitKey(0)

#Video Read
# capture= cv.VideoCapture(0)
# while True:
#     isTrue, frame= capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

#Resize image and video

def RescaleFrame(frame, scale=0.1):
    width= int(frame.shape[1]* scale)
    height= int(frame.shape[0]* scale)

    dimensions= (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#video
capture= cv.VideoCapture('Videos/me.mp4')
while True:
    isTrue, frame= capture.read()
    cv.imshow('original video', frame)
    cv.imshow('resized video', RescaleFrame(frame))

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()