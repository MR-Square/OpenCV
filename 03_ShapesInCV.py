'''
In this program we will see how to draw any shapes using opencv and write any text on images.
'''
import cv2 as cv
import numpy as np

# ----------------------------------------------
# creating and printing a blank img
blank_img = np.zeros((500,1000,3), dtype='uint8')
'''
500 is height of img.
1000 is width of img.
3 is number of color channels.
uint8 is a datatype for img.
'''
cv.imshow("blank img",blank_img)
cv.waitKey(1000)

# ----------------------------------------------
# 1) Painting the whole window of img.
blank_img[:] = 255,0,0
'''
[:] is for coloring all the pixcel of img.
255 is for blue.
0 is for green.
0 is for red.
'''
cv.imshow("Blue-color img",blank_img)
cv.waitKey(2000)

# ----------------------------------------------
# 2) Painting some part of img window.
blank_img[100:400,10:400] = 250,243,42
'''
100 is a distance between window's top and top border of shape.( or top margin)
400 is a distance between top border and bottom border of shape.( or height of shape)
10 is a distance between window's left and left border of shape.( or left margin)
4000 is a distance between left border and right border of shape.( or width of shape)
Here background color of window is blue because we did it blue above.
'''
cv.imshow("Some colored part of window",blank_img)
cv.waitKey(2000)

# Task-1 : Draw a shape with rgb value : rgb(78, 237, 102).
# Task-2 : Change the background color to rgb(240, 55, 203).

# ----------------------------------------------
# 3) Drawing a rectangle shape.
img = np.zeros((500,500,3), dtype='uint8')
cv.rectangle(img,(20,20),(100,100),(0,0,255),2)
'''
img - name of img window on which you want to draw rectangle.
(20,20) - top-left point of rectangle.
(100,100) - bottom-right point of rectangle.
(0,0,255) - color of border of rectangle.
2 - thickness of border.
(if you will give -1/cv.FILLED insted of 2 then rectangle will be filled with
 color which u mention for border.)
'''
cv.imshow("img with rectangle shape",img)
cv.waitKey(2000)
# There is one difference between point no 2 and 3 and that is by using point no 2
# you can draw a rectangle which is filled with color and by using point no 3 you 
# can draw a hollow rectangle.

# ----------------------------------------------
# 4) Drawing a circle.
img = np.zeros((500,500,3), dtype='uint8')
cv.circle(img,(250,250),50,(200,150,100),2)
cv.imshow("Circle",img)
cv.waitKey(2000)

# ----------------------------------------------
# 5) Drawing a line.
img = np.zeros((500,500,3), dtype='uint8')
cv.line(img,(50,100),(400,100),(255,255,255),4)
cv.imshow("Line",img)
cv.waitKey(2000)

# ----------------------------------------------
# 6) Printing some text.
img = np.zeros((1000,1300,3), dtype='uint8')
cv.putText(img,'Congratulation You have completed Shapes and Text lession.',(10,250),cv.FONT_HERSHEY_PLAIN,2.5,(255,255,255),3)
cv.imshow("Text img",img)
cv.waitKey(0)