from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from Dashboard import dashboard
import os

class Teacher_Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x525+300+200")
        self.root.title("नूतन मराठी विद्यालय") #Creating 1st window and fixing its geometry area
        self.root.configure(bg="#fff")
        self.root.resizable(False,False)
    
        #bg image
        img1=Image.open(r"F:\project\AI ML\Attemdance_system\Images\Login.jpg")
        img1=img1.resize((400,525),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=400,height=525)
        
        frame=LabelFrame(self.root,font=("times new roman",12,"bold"),bg='white',fg='white')
        frame.place(x=400,y=80,width=300,height=300)
        
        heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=("times new roman",20,"bold"))
        heading.place(x=90,y=0)
            
        def on_enter(e):
            userentry.delete(0,'end')
            
        def on_leave(e):
            name=userentry.get()
            if name=='':
                userentry.insert(0,'Username')
                     
        userentry= Entry(frame,width=25,fg='black',border=2,bg='white',font=("times new roman",12))
        userentry.place(x=50,y=80)
        userentry.insert(0,'Username')
        userentry.bind('<FocusIn>',on_enter)
        userentry.bind('<FocusOut>',on_leave)
        
        def on_enter(e):
            userpass.delete(0,'end')
            
        def on_leave(e):
            name=userpass.get()
            if name=='':
                userpass.insert(0,'Password')
        
        userpass= Entry(frame,width=25,fg='black',border=2,bg='white',font=("times new roman",12))
        userpass.place(x=50,y=130)
        userpass.insert(0,'Password')
        userpass.bind('<FocusIn>',on_enter)
        userpass.bind('<FocusOut>',on_leave)
        
        def login():
            username=userentry.get()
            password=userpass.get()
            
            if username=='admin' and password=='admin123':
                messagebox.showinfo("Sucess","Logging in",parent=self.root)
                self.new_window=Toplevel(self.root)
                self.app=dashboard(self.new_window)
                
            else:
                messagebox.showerror("Error","Wrong password!!",parent=self.root)
        
        button_login=Button(frame,width=20,pady=7,text='Login',command=login,bg='#57a1f8',fg='white',border=0)
        button_login.place(x=70,y=204)
        
if __name__=="__main__":
    root=Tk()
    obj=Teacher_Face_Recognition_System(root)
    root.mainloop()
    
