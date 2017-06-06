import cv2 as cv
import numpy as np

img = cv.imread('foto.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)

minLineLength = 100
maxLineGap = 10
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv.imwrite('houghlines5.jpg',img)