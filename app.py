from tkinter import *
from PIL import ImageTk, Image
import cv2
from sample import *
from showPhotos import *

class AttendaceApp:

    def __init__(self, window, title):
        self.window = window
        self.title = title
        window.title(self.title)
        window.geometry("500x500")
        window.iconbitmap("OpenCV\icon.ico")
        self.sp = PhotoImage(file="OpenCV/appimages/sample.png")
        self.sp_r = self.sp.subsample(8,8)

        # self.label = Label(window, image=self.sp)
        # self.label.pack()

        self.TrainData  = Button(window, image=self.sp_r, width=100, height=100, command=lambda:sampleDataWin())
        self.TrainData.grid(row=0, column=0)
        self.labelsample = Label(window, text="Take Sample")
        self.labelsample.grid(row=1, column=0)
        self.showPhotos  = Button(window, text="Show Student Photos", command=lambda:showPhotosWin())
        self.showPhotos.grid(row=2, column=0)
        self.TrainData  = Button(window, text="Train Data", command=lambda:trainData())
        self.TrainData.grid(row=3, column=0)
        self.FaceRecog  = Button(window, text="Face Recognition", command=lambda:faceRecogniseWin())
        self.FaceRecog.grid(row=4, column=0)
           
def sampleDataWin():
    sample = Tk()
    at = SampleApp(sample, "Year 11")
    sample.mainloop()

def faceRecogniseWin():
    at = ShowPhotoApp(root, "Year 11")
    at.face_recog()

def showPhotosWin():
    st = Tk()
    at = ShowPhotoApp(st, "Year 11")
    at.show(st, "Year 11")

def trainData():
    at = ShowPhotoApp(root, "Year 11")
    at.trainDataSample()


root = Tk()
at = AttendaceApp(root, "Year 11")
root.mainloop()