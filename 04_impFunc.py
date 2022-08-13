'''
In this program we will see some important functions which is used in opencv
'''
import cv2 as cv

def RescaleFrame(frame,scale=0.75):
    ''' This function will work for img,vid and live vid.'''
    return cv.resize(frame, (int(frame.shape[1]*scale),int(frame.shape[0]*scale)),interpolation=cv.INTER_AREA)
# --------------------------------------------------------------------------
# 1) Converting img to grayscale.
img = RescaleFrame(cv.imread('my.jpg'),0.4)
cv.imshow("img",img)

image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray img",image)
cv.waitKey(2000)

# --------------------------------------------------------------------------
# 2) Blurring an img
blurImg = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur img',blurImg)
'''
image - name of img whose have to blurred
(5,5) - how much blur you want to do.These value must be odd numbers only.

'''
b = cv.GaussianBlur(image,(35,35),cv.BORDER_DEFAULT)
cv.imshow('second blur',b)
cv.waitKey(2000)

# --------------------------------------------------------------------------
# 3) Edge Csacade
img = RescaleFrame(cv.imread('my.jpg'),0.4)
cas1 = cv.Canny(img,100,100)
cas2 = cv.Canny(blurImg,100,90)
cas3 = cv.Canny(b,90,90)
cv.imshow('First cascade',cas1)
cv.imshow('Second cascade',cas2)
cv.imshow('Third cascade',cas3)
cv.waitKey(2000)

# --------------------------------------------------------------------------
# 4) Dilating image
dilated = cv.dilate(img,(3,3),iterations=1)
cv.imshow('dilated', dilated)
cv.waitKey(2000)

# --------------------------------------------------------------------------
# 5) Eroding
eroded = cv.erode(img,(5,5),iterations=3)
cv.imshow('eroded', eroded)
cv.waitKey(2000)

# --------------------------------------------------------------------------
# 6) Resizing img




















# --------------------------------------------------------------------------
# --------------------------------------------------------------------------