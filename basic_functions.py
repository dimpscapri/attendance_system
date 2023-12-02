import cv2 as cv

img = cv.imread("OpenCV\images\cat.jpg")
cv.imshow("CAT", img)

#Grayscale images
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY CAT", gray_image)

#Blur images
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur Cat", blur)

#Edge Cascades
canny = cv.Canny(img, 125,175)
cv.imshow("Canny", canny)

#Resize image
resized = cv.resize(img, (1500,1500), interpolation=cv.INTER_CUBIC )
cv.imshow("Rezised", resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)