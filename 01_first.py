# First run the following command to install open cv in ur maching
# pip install opencv-contrib-python

# Then run this one as well
# pip install caer

# READING IMAGE AND VIDEO
from operator import itruediv
import cv2 as cv

# to read an img we use .imread() which take the path of img as parameter.
firstImg = cv.imread('my.jpg')

# To print that img we use .imshow() which take window name as first parameter and variable name
# as second parameter.
cv.imshow('Raza with Hasnain',firstImg)
cv.waitKey(0)


# reading vid
# integer 0 is refer for web camera
# To read a video we use .VideoCapture() which take integer/path as a parameter.
firstVid = cv.VideoCapture('project.mp4')

# Let's run that video
while True:
    isTrue, frame = firstVid.read()
    cv.imshow('project',frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  

firstVid.release()
cv.destroyAllWindows()
