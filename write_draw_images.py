import cv2 as cv
import numpy as np
#height, width and the colour channels
blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("Blank", blank)
# cat = cv.imread('OpenCV\images\cat.jpg')
# cv.imshow("Cat", cat)

#paint the picture as green
# blank[200:300,300:400] = 0,0,255
# cv.imshow("Green",blank)

#Draw a rectangle
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=2)
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=-1)
# cv.rectangle(blank, (0,0),(blank.shape[1]//2,blank.shape[1]//2),(0,255,0),thickness=-1)
# cv.imshow("Rectangle", blank)

#Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40, (0,0,255), thickness=3)
# cv.imshow("Circle", blank)

#Draw a Line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=3)
# cv.imshow("Line", blank)

cv.putText(blank, "HELLO", (200,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),2 )
cv.imshow("TEXT", blank)

cv.waitKey(0)