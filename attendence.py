import os
import cv2
import numpy 

base_folder = "OpenCV/images"
labels = []
images = []
labels_dict = {}

i = 0
for person in os.listdir(base_folder):
    labels_dict[i] = person
    
    for image_file in os.listdir(f"{base_folder}/{person}"):
        image_path = f'{base_folder}/{person}/{image_file}'
        print(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        images.append(image)
        labels.append(i)
    i+=1
print(labels_dict)
print(labels)
print(images)

def train_face_recognizer(images, labels):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(images, numpy.array(labels))
    return recognizer

recognizer = train_face_recognizer(images, labels)

print (recognizer)


cap  = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#faces = face_cascade.detectMultiScale("gray", 1.3, 5)

while True:
    ret, frame = cap.read()
    #print(ret, frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)

    for x,y,w,h in faces:
        #ROI-- Region Of Interest
        roi_gray = gray[y:y+h, x:x+h]
        #print(roi_gray)
        label, confidence  = recognizer.predict(roi_gray)
        # print(label, confidence)

        if confidence>50:
            name = labels_dict[label]
            print(name)
            
