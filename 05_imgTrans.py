'''
In this program we will see about img translation,transformation,rotation,resizing
'''
import cv2 as cv
import numpy as np

img = cv.imread('my.jpg')

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

'''
-x --> left
-y --> up
x  --> right
y  --> down
'''
translated1 = translate(img,100,100)
cv.imshow('translated',translated1)
cv.waitKey(1000)

# Rotation
# Resizing
# Flipping
flip = cv.flip(img,1)
'''
0 - fliping img vertically i.e over the x-axis.
1 - fliping img horizontally i.e over the y-axis.
-1 - flipng img both vertically and horizontally.
'''
cv.imshow('fliped',flip)
cv.waitKey(0)