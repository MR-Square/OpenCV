import cv2 as cv
import numpy as np

img = cv.imread('cat.jpeg')
cv.imshow('cat',img)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray cat',grayImg) 

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)
cv.waitKey(1000)

# 01:01:00