from cProfile import label
from cgitb import text
from email import contentmanager, message
from email.mime import image
import fractions
from http import client
from itertools import count
from msilib import add_data
from multiprocessing import connection
from multiprocessing.sharedctypes import Value
from operator import countOf
from optparse import Values
from socket import fromfd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from DEMPP import pay
from dempd import dept
import pymongo
from pymongo import collection
from PIL import Image,ImageTk
from demp import Employ
from employee import Employee
from department import Department
from payroll import Payroll

class Main:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1420x720+0+0")
                self.root.title("Employee Management System")

                lbl_title=Label(self.root,text="     EMPLOYEE MANAGEMENT SYSTEM",font=('times new roman',35,'bold'),fg='darkblue',bg='white')
                lbl_title.place(x=0,y=0,width=1300,height=45)

                image_logo=Image.open('jspm.ico.png')
                image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
                self.photo_logo=ImageTk.PhotoImage(image_logo)

                self.logo=Label(self.root,image=self.photo_logo)
                self.logo.place(x=200,y=0,width=50,height=50)

        #Main frame

                Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
                Main_frame.place(x=10,y=46,width=1250,height=600)

        # Lower Frame

                lower_frame=Frame(Main_frame,bd=2,relief=RIDGE,bg='white')
                lower_frame.place(x=10,y=230,width=1225,height=350)

                # Left frame

                
                left_frame=Frame(lower_frame,bd=2,relief=RIDGE,bg='white')
                left_frame.place(x=5,y=5,width=900,height=338)

                # Right frame

                right_frame=Frame(lower_frame,bd=2,relief=RIDGE,bg='white')
                right_frame.place(x=905,y=5,width=310,height=338)



        



    


                # Images
                image_1=Image.open('b.jpg')
                image_1=image_1.resize((400,200),Image.ANTIALIAS)
                self.photo_1=ImageTk.PhotoImage(image_1)

                self.im1=Label(Main_frame,image=self.photo_1)
                self.im1.place(x=0,y=5,width=400,height=220)

                image_2=Image.open('c.jpg')
                image_2=image_2.resize((500,200),Image.ANTIALIAS)
                self.photo_2=ImageTk.PhotoImage(image_2)

                self.im2=Label(Main_frame,image=self.photo_2)
                self.im2.place(x=402,y=5,width=500,height=220)

                image_3=Image.open('MainFrame_Images/a.jpeg')
                image_3=image_3.resize((400,200),Image.ANTIALIAS)
                self.photo_3=ImageTk.PhotoImage(image_3)

                self.im3=Label(Main_frame,image=self.photo_3)
                self.im3.place(x=904,y=5,width=400,height=220)


# Entities

                entities=Label(left_frame,font=('arial',17,'bold'),text='Entities :-',fg='red',bg='white')
                entities.place(x=0,y=0)

        #1

                emp=Image.open('MainFrame_Images/OIP.jpg')
                emp=emp.resize((250,100),Image.ANTIALIAS)
                self.photo_4=ImageTk.PhotoImage(emp)

                self.img1=Label(left_frame,image=self.photo_4)
                self.img1.place(x=60,y=30,width=250,height=100)

                btn_employee =Button(left_frame,text='Employee',command=self.emp_details,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
                btn_employee.place(x=140,y=150,width=100,height=30)


        

                
               


                


        #2

                dep=Image.open('MainFrame_Images/R.png')
                dep=dep.resize((250,120),Image.ANTIALIAS)
                self.photo_5=ImageTk.PhotoImage(dep)

                self.img2=Label(left_frame,image=self.photo_5)
                self.img2.place(x=550,y=30,width=250,height=120)


                btn_department =Button(left_frame,text='Department',command=self.dep_details,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
                btn_department.place(x=630,y=150,width=120,height=30)

        


        


#3

        
                pay=Image.open('MainFrame_Images/P.jpg')
                pay=pay.resize((250,120),Image.ANTIALIAS)
                self.photo_6=ImageTk.PhotoImage(pay)

                self.img3=Label(left_frame,image=self.photo_6)
                self.img3.place(x=330,y=160,width=250,height=120)

                btn_payroll =Button(left_frame,text='Payroll',command=self.pay_details,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
                btn_payroll.place(x=400,y=280,width=100,height=30)


        # Info/Credits

                credits=Label(right_frame,font=('arial',17,'bold'),text='Credits :-',fg='red',bg='white')
                credits.place(x=0,y=0)


                info1=Label(right_frame,font=('arial',12,'bold'),text='Group No – 14',fg='black',bg='white')
                info1.place(x=100,y=40)

                info3=Label(right_frame,font=('arial',12,'bold'),text='S190408550 – Shreyash Nimonkar',bg='white')
                info3.place(x=20,y=70)

                info4=Label(right_frame,font=('arial',12,'bold'),text='S190408544 – Tejas Lankeshwar',bg='white')
                info4.place(x=20,y=90)

                info5=Label(right_frame,font=('arial',12,'bold'),text='S190408551 – Arihant Ostwal',bg='white')
                info5.place(x=20,y=110)

                info2=Label(right_frame,font=('arial',12,'bold'),text='S190408549 – Rohan Nimbalkar',bg='white')
                info2.place(x=20,y=130)

                info6=Label(right_frame,font=('arial',12,'bold'),text='Under the guidance of ',bg='white')
                info6.place(x=60,y=170)

                info7=Label(right_frame,font=('arial',17,'bold'),text='Prof .A.K.Gupta',bg='white')
                info7.place(x=70,y=200)



# Exit button


                btn_exit =Button(right_frame,text='EXIT',command=self.exit,font=('arial',15,'bold'),width=24,bg='red',fg='white')
                btn_exit.place(x=5,y=270)




        def emp_details(self):
                self.new_window1=Toplevel(self.root)
                self.app1=Employ(self.new_window1)


        def dep_details(self):
                self.new_window2=Toplevel(self.root)
                self.app2=dept(self.new_window2)


        def pay_details(self):
                self.new_window3=Toplevel(self.root)
                self.app3=pay(self.new_window3)


        def exit(self):
                self.root.destroy()
        


















        










if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()