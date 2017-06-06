import numpy as np, cv2 as cv
import math

def angVetor(u, v):
    modulo_u = math.sqrt((math.pow(u[0],2) + math.pow(u[1],2)))
    modulo_v = math.sqrt((math.pow(v[0],2) + math.pow(v[1],2)))
    x = modulo_u * modulo_v
    uXv = u[0] * v[0] + u[1] * v[1]
    cosO = uXv / x
    angO = math.acos(cosO)
    return angO

frames = cv.imread("foto1.jpg")
imgray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
frames = cv.drawContours(frames, contours, -1, (0,255,0), 1)
print angVetor([170,  71],[170, 380])
print("-----------")
while True:
    cv.imshow('Identificador', frames)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
