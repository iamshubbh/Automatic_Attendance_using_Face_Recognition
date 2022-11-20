import os
from tkinter import *
import tkinter
from tkinter import font, ttk
from tokenize import String
from PIL import Image, ImageTk
from face_recognition import Face_Recognition
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System using Face Recognition")


        #img1
        img = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\black.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #img2
        img1 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\black.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #img3
        img2 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\black.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #background image
        img3 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\bg.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=-60,y=0,width=1530,height=45)

 
    

        #student button
        img4 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\student_button.jpg")
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=70,y=70,width=220,height=220)
       
        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=70,y=250,width=220,height=40)
        
        #detect face button
        img5 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\face.png")
        img5 = img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=220,height=220)
       
        b1_1 = Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=220,height=40)

        #attendance face button
        img6 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\ATTENDANCE.webp")
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=700,y=70,width=220,height=220)
       
        b1_1 = Button(bg_img,text="ATTENDANCE",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=220,height=40)

        #help button
        img7 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\help_desk.png")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=70,width=220,height=220)
       
        b1_1 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=250,width=220,height=40)

        #train button
        img8 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\train.jpeg")
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=70,y=300,width=220,height=220)
       
        b1_1 = Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=70,y=480,width=220,height=40)

        #PHOTO button
        img9 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\photo.png")
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=400,y=300,width=220,height=220)
       
        b1_1 = Button(bg_img,text="PHOTO",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=480,width=220,height=40)

        #developer button
        img10 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\developer.png")
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=220,height=220)
       
        b1_1 = Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=480,width=220,height=40)

        #exit button
        img11 = Image.open(r"D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\exit.png")
        img11 = img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=220,height=220)
       
        b1_1 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=480,width=220,height=40)

    
    def open_image(self):
        os.startfile("D:\Minor Project\Automatic Attendance System Using Facial Recognition\data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit the screen ?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return    


    # Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)        

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)        


      



        
        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()