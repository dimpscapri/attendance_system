import cv2 as cv
import numpy as np
# cat = cv.imread("OpenCV\images\cat.jpg")
# cv.imshow("CAT", cat)

blank = np.zeros((500,500,3), dtype="uint8")
# cv.imshow("Blank", blank)


#paint the picture red
# blank[:] = 128,128,0
# cv.imshow("Teal", blank)

# blank[200:300,300:400] = 255,0,0
# cv.imshow("Small Patch", blank)

# Draw a rectangle
# cv.rectangle(blank, (0,0), (250,300),(128,128,0), thickness=2)
#Filled Rectangle
#cv.rectangle(blank, (0,0), (250,300),(128,128,0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(200,128,0), thickness=-1)

#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (240,0,140), thickness=-1 )



# Draw Line
# cv.line(blank, (250,0), (250,500), (255,255,255), thickness=5)

#Add Text
cv.putText(blank, "Hello", (210,250), cv.FONT_HERSHEY_TRIPLEX, 2.0, (255, 255, 2550), thickness=2)

cv.imshow("Rect", blank)

cv.waitKey(0)