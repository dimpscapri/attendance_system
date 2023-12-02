import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import cv2
import numpy as np
import sqlite3
from time import strftime
from datetime import datetime
import csv
class ShowPhotoApp:

    def __init__(self, window, title):
        username = StringVar()
        self.window = window
        self.title = title
        window.title(self.title)
        window.geometry("1024x900")
        window.iconbitmap("OpenCV\icon.ico")
        

    def trainDataSample(self):
        path = "OpenCV\images"
        faces = []
        ids = []

        # Get a list of all files and directories in the specified path
        files_and_directories = os.listdir(path)

        # Filter out only the directories from the list of files and directories
        for d in files_and_directories:
            if os.path.isdir(os.path.join(path, d)):
                directory_path = os.path.join(path, d)
                for image in os.listdir(directory_path):
                    id = int(os.path.split(image)[1].split('.')[1])
                    # print(os.path.split(image)[1].split('.'))
                    ids.append(id)
                    file_path = os.path.join(directory_path, image)
                    img = Image.open(file_path).convert('L')
                    imageNP = np.array(img, 'uint8')
                    faces.append(imageNP)
                    
                    cv2.imshow("Training", imageNP)
                    cv2.waitKey(1) == 13
        ids = np.array(ids, dtype=np.int32)
        # Train
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("OpenCV\classifier.xml")
        cv2.destroyAllWindows()
        self.lbl = Label(self.window, text="Training Completed",
                         font=("Arial", 14), fg="blue")
        self.lbl.pack()
        

    def show(self, window, title):
        self.window = window
        self.title = title
        window.title(self.title)
        self.lbl = Label(self.window, text="Student Data",
                         font=("Arial", 14), fg="blue")
        self.lbl.pack()
        # t = ShowPhotoApp(root, "Year 11")
        path = "OpenCV\images"

        # Get a list of all files and directories in the specified path
        files_and_directories = os.listdir(path)

        # Filter out only the directories from the list of files and directories
        for d in files_and_directories:
            if os.path.isdir(os.path.join(path, d)):
                lbl = Label(self.window, text=d, font=("Arial", 14), fg="blue")
                lbl.pack()
                directory_path = os.path.join(path, d)
                for f in os.listdir(directory_path):
                    print("___"+os.path.join(directory_path, f)+"___")
                    if os.path.isfile(os.path.join(directory_path, f)):
                        image = Image.open(os.path.join(directory_path, f))
                        # image = Image.open('..\OpenCV\images\Dimple\Dimple.1.jpg')
                        photo = ImageTk.PhotoImage(image)
                        # photo = ImageTk.PhotoImage(image=Image.fromarray(image))
                        lbl = Label(self.window, image=photo)
                        lbl.pack()
                        # lbl.image = photo
                        break

    def mark_attendence(self,id, name):
        current_date = datetime.now().strftime('%Y-%m-%d')
        filename = f"OpenCV/sheets/{current_date}.csv"
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
        try:
            with open(filename,"r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                if (str(id) not in name_list) and (name not in name_list):
                    f.writelines(f"\n{id},{name},{dtString},{d1},Present")
        except FileNotFoundError:
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([id,name,dtString,d1,"Present"])

    
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours,color, text, clf):
            conn = sqlite3.connect("Attendence.db")
            c = conn.cursor()
            if img is None:
                print("Failed to load the image.")
            else:
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
                coord =[]

                for (x,y,w,h) in features:
                    
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    
                    confidence = int(100*(1-predict/300))
                    c.execute("SELECT StudentName FROM Student WHERE id = :specific_id", {'specific_id': id})
                    result = c.fetchone()
                    if result:
                        student_name = result[0]
                    # print(student_name)  
                    if confidence>77:
                        cv2.putText(img,f"Name:{student_name}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        self.mark_attendence(id,student_name)
                    coord =[x,y,w,h]
                return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCasacade = cv2.CascadeClassifier("OpenCV\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("OpenCV\classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCasacade)
            if img is None or img.shape[0] == 0 or img.shape[1] == 0:
                print("Image not loaded or empty.")
            else:
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1)==13:
                    break
        video_cap.release()
        cv2.destroyAllWindows()
# st = Tk()
# at = ShowPhotoApp(st, "Year 11")
# at.show(st, "Year 11")
      
