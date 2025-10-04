import cv2 as cv
import matplotlib.pyplot as plt


image= cv.imread('Photos/cat.jpg')
cv.imshow('Image', image)
#gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
#bgr_hist= cv.calcHist([image], [0], None, [256], [0,256])
#gray_hist= cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Gray Histogram')
# plt.xlabel('bins')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist, color='b')
# plt.xlim([0,256])   
# plt.show()


#colored histogram
color= ('b', 'g', 'r')
for i, col in enumerate(color):
    hist= cv.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist, color=col)

plt.xlim([0,256])
plt.xlabel('bins')
plt.ylabel('no. of pixeles')
plt.title('Colored histogram')
plt.xlim([0,256])
plt.show()
cv.waitKey(0)