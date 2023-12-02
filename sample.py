from tkinter import *
from PIL import ImageTk, Image
from read import *
from tkinter import messagebox
import sqlite3

class SampleApp:

    def __init__(self, window, title):
        conn = sqlite3.connect("Attendence.db")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                id INTEGER PRIMARY KEY,
                StudentName text
            )""")
        username = StringVar()
        self.window = window
        self.title = title
        window.title(self.title)
        window.geometry("300x300")
        window.iconbitmap("OpenCV\icon.ico")
        self.lbl = Label(window, text="Train Data", font=("Arial",14), fg="blue")
        self.namelbl = Label(window, text="Enter Student Name", font=("Arial",12))
        self.UserNameEntry = Entry(window)
        self.TakePhotoBtn  = Button(window, text="Take Photo Sample", command=lambda:insertStudentData(self))
        self.lbl.grid(row=0, columnspan=2)
        self.namelbl.grid(row=1, column=0)
        self.UserNameEntry.grid(row=1, column=1)
        self.TakePhotoBtn.grid(row=2, columnspan=2)

        def insertStudentData(self):
            c = conn.cursor()
            c.execute("INSERT INTO Student (StudentName) VALUES (:StudentName)",
            {
                'StudentName': self.UserNameEntry.get()
            }
            )
            conn.commit()
            # Get the ID of the last inserted row
            last_id = c.lastrowid
            print("The ID of the last inserted row is:", last_id)
            sampleData(self, last_id)

        def sampleData(self, id):
            print(self.UserNameEntry.get())
            if self.UserNameEntry.get() == "":
                messagebox.showerror("Missing","Enter the Name for the user")
            else:
                getData(self.UserNameEntry.get(), id)
                messagebox.showinfo("Success","Picture Sample Collected!")



# root = Tk()
# at = TrainApp(root, "Year 11")
# root.mainloop()