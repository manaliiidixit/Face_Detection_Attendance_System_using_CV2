from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
from traindata import Train
from face_recognization import face_recognization
from developer import Developer
from attendance import Attendance

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System") #Creating 1st window and fixing its geometry area
        
        #bg image
        img1=Image.open(r"F:\project\AI ML\Attemdance_system\Images\bg1.jpg")
        img1=img1.resize((1530,790),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",35,"bold"),bg="yellow",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Contact Us",font=("times new roman",12,"bold"))
        frame.place(x=300,y=200,width=500,height=300)
        
        label=Label(frame,text="nishantmahalkari@gmail.com",font=("times new roman",28,"bold"))
        label.grid(row=0,column=0,padx=10)
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()