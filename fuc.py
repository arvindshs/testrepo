import cv2 as cv

img=cv.imread('photos/rose.jpg')
cv.imshow("rose",img)

#1.gray-channel

#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

# 2--blur the image

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

# 3.edge cascades

edge=cv.Canny(blur,125, 175)
#cv.imshow("ege",edge)

#4-- dailating the image

dia=cv.dilate(edge, (3,3),iterations=1)
#cv.imshow("dia",dia)
#5--eroding
erode=cv.erode(dia,(3,3),iterations=1)
cv.imshow('erode',erode)


#6.resize

resize=cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('re',resize)
#6 cropping

crop=img[50:200,200:400]
cv.imshow('crp',crop)
cv.waitKey(0)