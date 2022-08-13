# import cv2 as cv

# # reading img
# img  = cv.imread('my.jpg')

# # printing img
# cv.imshow('Raza',img)

# # increasing waiting time
# cv.waitKey(0)

# # To rescale fram of img
# def rescaleFrame(frame,scale=0.75):  # 0.75 is default size in this case.
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width,height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# # Resizing img
# ResizedImg = rescaleFrame(img,scale=0.2)
# cv.imshow('Rezied Image',ResizedImg)




# vid = cv.VideoCapture('project.mp4')
# while True:
#     isTrue, frame = vid.read()
#     resizeFrame = rescaleFrame(frame)

#     cv.imshow('Video',frame)     
#     cv.imshow('Resize Video',resizeFrame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# vid.release()
# cv.destroyAllWindows()


# ====================================
import cv2 as cv

def RescaleFrame(frame,scale=0.75):
    ''' This function will work for img,vid and live vid.'''
    # return cv.resize(frame, (int(frame.shape[1]*scale),int(frame.shape[0]*scale)),interpolation=cv.INTER_AREA)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # .shape[1] is for frame width
    # .shape[0] is for frame height

    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# Resizing images
img = cv.imread('my.jpg')
cv.imshow("Image",img)
cv.imshow('resize image',RescaleFrame(img,.2))



# Resizing video
vid = cv.VideoCapture('project.mp4')



while True:
    isTrue, frame = vid.read()
    resize_frame = RescaleFrame(frame)
    cv.imshow("vid",frame)
    cv.imshow("Resized vid",resize_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()

# time: 19:46