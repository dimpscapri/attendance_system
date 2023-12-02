import cv2 as cv

img= cv.imread("OpenCV/images/cat_large.jpg")

def rescale_image(frame, scale = 0.40):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA )


cv.imshow("CAT", rescale_image(img, scale=0.20 ))

cv.waitKey(0)
