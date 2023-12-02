import cv2 as cv
import os 

capture = cv.VideoCapture(0)

#Rescale Frame
def img_scale(frame, scale = 0.40):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")
def face_cropped(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)

    for (x,y,w,h) in faces:
        face_cropped = img[y:y+h, x:x+w]
        return face_cropped

def getData(user):
    cap = cv.VideoCapture(0)
    img_id = 0
    fileNamePath = "OpenCV/images/"+str(user)
    mode = 0o666
    os.mkdir(fileNamePath, mode)
    while True:
        ret, my_frame = cap.read()
        if face_cropped(my_frame) is not None:
           img_id+=1
        face = img_scale(my_frame)
        face=cv.cvtColor(face, cv.COLOR_BGR2GRAY)
        finalfile = fileNamePath + "/"+str(user)+"."+str(img_id)+".jpg"
        cv.imwrite(finalfile, face)
        cv.imshow("Cropped Face", face)

        if cv.waitKey(1) == 13 or int(img_id) == 100:
            break
    cap.release()
    cv.destroyAllWindows()



