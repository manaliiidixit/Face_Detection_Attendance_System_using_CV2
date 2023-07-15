from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
from traindata import Train
from face_recognization import face_recognization
from developer import Developer
from attendance import Attendance
from help import Help
import os

class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("नूतन मराठी विद्यालय") #Creating 1st window and fixing its geometry area
        
        #bg image
        img1=Image.open(r"F:\project\AI ML\Attemdance_system\Images\bg1.jpg")
        img1=img1.resize((1530,790),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="नूतन मराठी विद्यालय",font=("times new roman",35,"bold"),bg="yellow",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=65)
        
        #student button
        
        img4=Image.open(r"F:\project\AI ML\Attemdance_system\Images\student.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1= Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b2= Button(bg_img,text="विद्यार्थी माहिती",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b2.place(x=200,y=300,width=220,height=40)
        
        #Detect Face button
        
        img5=Image.open(r"F:\project\AI ML\Attemdance_system\Images\face detection.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b3= Button(bg_img,command=self.face_recognization,image=self.photoimg5,cursor="hand2")
        b3.place(x=500,y=100,width=220,height=220)
        
        b4= Button(bg_img,text="हजेरी लावा",command=self.face_recognization,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b4.place(x=500,y=300,width=220,height=40)
        
        #Attendance Face button
        
        img6=Image.open(r"F:\project\AI ML\Attemdance_system\Images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b5= Button(bg_img,command=self.Attendance,image=self.photoimg6,cursor="hand2")
        b5.place(x=800,y=100,width=220,height=220)
        
        b6= Button(bg_img,text="हजेरी माहिती पाहा ",command=self.Attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=800,y=300,width=220,height=40)
        
        #Help Face button
        
        img7=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b5= Button(bg_img,command=self.help,image=self.photoimg7,cursor="hand2")
        b5.place(x=1100,y=100,width=220,height=220)
        
        b6= Button(bg_img,command=self.help,text="मदत",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=1100,y=300,width=220,height=40)
        
        #Train Face button
        
        img8=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b5= Button(bg_img,image=self.photoimg8,command=self.Train,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)
        
        b6= Button(bg_img,text="फोटो तपासणी ",command=self.Train,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=200,y=580,width=220,height=40)
        
        #Photos Face button
        
        img9=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b5= Button(bg_img,command=self.openFile,image=self.photoimg9,cursor="hand2")
        b5.place(x=500,y=380,width=220,height=220)
        
        b6= Button(bg_img,text="फोटो पहा",command=self.openFile,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=500,y=580,width=220,height=40)
        
    
        #Developer Face button
        
        img10=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b5= Button(bg_img,command=self.Developer,image=self.photoimg10,cursor="hand2")
        b5.place(x=800,y=380,width=220,height=220)
        
        b6= Button(bg_img,text="Developer Contact ",command=self.Developer,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=800,y=580,width=220,height=40)
        
        #Exit Face button
        
        img11=Image.open(r"F:\project\AI ML\Attemdance_system\Images\exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b5= Button(bg_img,command=self.Close,image=self.photoimg11,cursor="hand2")
        b5.place(x=1100,y=380,width=220,height=220)
        
        b6= Button(bg_img,command=self.Close,text="बाहेर",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=1100,y=580,width=220,height=40)
        
    def Close(self):
        self.root.destroy()
        
        #functions
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
    def Train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_recognization(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognization(self.new_window)
        
    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def openFile(self):
        os.startfile("Data")
    
if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)
    root.mainloop()