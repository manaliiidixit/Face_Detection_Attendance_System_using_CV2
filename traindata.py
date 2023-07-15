from msilib.schema import SelfReg
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np 

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("नूतन मराठी विद्यालय") #Creating 1st window and fixing its geometry area
        
        #bg image
        img1=Image.open("./Images/bg1.jpg")
        img1=img1.resize((1530,790),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="Train Data Set",font=("times new roman",35,"bold"),bg="yellow",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Training button 1
        std_img_btn=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Traindata.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)
        
        #training Functions
    def train_classifier(path):
        data_dir=("Data")
        imagepath=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for imagepath in imagepath:
            img=Image.open(imagepath).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(imagepath)[-1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #training Classifier
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.yml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Classifier Trained Successfully!")

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()