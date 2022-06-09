# importing required library
import cv2
import numpy as np
# loading input video
cap = cv2.VideoCapture('obj04.mp4')

def is_contour_bad(c):
    pass

while True:
    # reading imput frame
    ret, frame = cap.read()
    # To get the height and width of input frame
    h,w = frame.shape[:2]
    # To resize the frame
    ratio = 1200/w
    dim = (1200,int(h*ratio))
    frame = cv2.resize(frame,dim)
    # To make input frame smooth
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    gray = cv2.filter2D(src=frame,ddepth=-1,kernel=kernel)
    # To change the color of frame into gray scale format
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Using gaussian blur for removing noise
    gray = cv2.GaussianBlur(gray, (9, 9), 0)
    cv2.imshow("frame",gray)

    #ret, thresh = cv2.threshold(gray,175,220,cv2.THRESH_BINARY_INV)
    # To perform canny edge detection
    canny = cv2.Canny(gray,0,150)
    cv2.imshow("frame", canny)
    new_background = np.zeros(frame.shape,np.uint8)
    new_frame = np.ones(frame.shape[:2],np.uint8)*255
    #cv2.imshow("frame",new_frame)

    # To find out the contour
    contour, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    sorted_contour = max(contour,key=cv2.contourArea)
    # To draw contour
    #cv2.drawContours(new_frame,sorted_contour,-1,(0,255,0),3)

    for con in range(len(contour)):
        if con !=1:
            cv2.fillConvexPoly(new_background,contour[con],(255,255,255))

    cv2.imshow('bitwise', new_background)

    # To hold the windows
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()