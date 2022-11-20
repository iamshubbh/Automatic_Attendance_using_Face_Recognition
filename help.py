from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance System using Face Recognition")

        title_lbl = Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-100,y=0,width=1530,height=45)

        img_top = Image.open("D:\Minor Project\Automatic Attendance System Using Facial Recognition\images\help-desk.png")
        img_top = img_top.resize((900,500),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-90,y=45,width=1500,height=700)

        
        dev_label=Label(f_lbl,text="Contact us:",font=("times new roman",14,"bold"))
        dev_label.place(x=90,y=5)

        dev_label1=Label(f_lbl,text="sshubhdeep12@gmail.com",font=("times new roman",14,"bold"))
        dev_label1.place(x=90,y=60)

        dev_label2=Label(f_lbl,text="harshraj8118@gmail.com",font=("times new roman",14,"bold"))
        dev_label2.place(x=90,y=85)

        dev_label3=Label(f_lbl,text="© 2022 by Shubhdeep & Harsh. All Rights Reserved. | Copyright | Terms of Use & Privacy Policy",font=("times new roman",14,"bold"))
        dev_label3.place(x=320,y=600)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 