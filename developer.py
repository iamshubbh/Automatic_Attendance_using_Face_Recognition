from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System using Face Recognition")

        title_lbl = Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-100,y=0,width=1530,height=45)

        img_top = Image.open("D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\Developer.jpg")
        img_top = img_top.resize((1500,640),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=700)

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=600,height=200)

        img_top1 = Image.open("D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\harsh.jpeg")
        img_top1 = img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=200,y=0,width=200,height=200)

        img_top2 = Image.open("D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\my_pic.jpeg")
        img_top2 = img_top2.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=0,y=0,width=200,height=200)

        img_top3 = Image.open(r"images\nancy.jpeg")
        img_top3 = img_top3.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=400,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Team",font=("times new roman",14,"bold"))
        dev_label.place(x=0,y=5)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()  
  