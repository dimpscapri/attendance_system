import cv2 as cv

capture = cv.VideoCapture("OpenCV/videos/cute-cat.mp4")


def rescale_image(frame, scale = 0.40):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA )

while True:
    isTrue, frame = capture.read()
    rescale_frame = rescale_image(frame)
    cv.imshow("My Web Cam",rescale_frame )
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()