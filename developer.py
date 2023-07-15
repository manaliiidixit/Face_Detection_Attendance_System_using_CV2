from tkinter import*
from tkinter import ttk
from traindata import Train
from PIL import Image,ImageTk
from student import student
from traindata import Train
from face_recognization import face_recognization
from attendance import Attendance
import os

class Developer:
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
        
        title_lbl=Label(bg_img,text="Developer Pannel",font=("times new roman",35,"bold"),bg="yellow",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"F:\project\AI ML\Attemdance_system\Images\nishant.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Nishant Mahalkari",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

         # Attendance System button 3
        att_img_btn=Image.open(r"F:\project\AI ML\Attemdance_system\Images\aniruddha.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=1170,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Aniruddha Jadhav",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=1170,y=380,width=180,height=45)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()