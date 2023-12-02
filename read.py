import cv2 as cv
import os

#Rescale Frame
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# def showVideo():
#     capture = cv.VideoCapture(0)
#     while True:
#         isTrue, frame = capture.read()
#         frame_scaled = rescaleFrame(frame)
#         cv.imshow('Video', frame_scaled)
#         if cv.waitKey(20) & 0xFF==ord('d'):
#             break
#     capture.release()
# # cv.destroyAllWindows()


face_cascade = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")
def face_cropped(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)

    for (x,y,w,h) in faces:
        face_cropped = img[y:y+h, x:x+w]
        return face_cropped
    
def getData(user, id):
    cap = cv.VideoCapture(0)
    img_id= 0
    fileNamepath = "OpenCV/images/"+str(user)
    mode = 0o666
    os.mkdir(fileNamepath, mode)
    while True:
       ret, my_frame = cap.read()
       if face_cropped(my_frame) is not None:
           img_id+=1
       face = rescaleFrame(my_frame)
       face = cv.cvtColor(face, cv.COLOR_BGR2GRAY) #grayscale
       finalfile = fileNamepath + "/"+str(user)+"."+str(id)+"."+str(img_id)+".jpg"
       cv.imwrite(finalfile, face)
    #    cv.putText(face,str(img_id),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
       cv.imshow("Cropped Face", face) 

       if cv.waitKey(1) == 13 or int(img_id) ==100:
           break 
    cap.release()
    cv.destroyAllWindows()
    