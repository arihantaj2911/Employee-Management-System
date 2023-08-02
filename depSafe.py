from cProfile import label
from cgitb import text
from email import contentmanager, message
from email.mime import image
import fractions
from http import client
import imp
from itertools import count
from msilib import add_data
from multiprocessing import connection
from multiprocessing.sharedctypes import Value
from operator import countOf
from optparse import Values
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk



class Department:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1420x720+0+0")
        self.root.title("Employee Management System - made by Shreyash")


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

        # Upper Frame

        Upper_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Department',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)



         # Lable and Entry fields

         #id

        lbl_empid=Label(Upper_frame,text='ID',font=('arial',15,'bold'),bg='white')
        lbl_empid.grid(row=0,column=0,pady=10,sticky=W)

        txt_empid=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_empid.grid(row=0,column=1,pady=10)


        # name

        lbl_name=Label(Upper_frame,text='Name',font=('arial',15,'bold'),bg='white')
        lbl_name.grid(row=2,column=0,pady=10,sticky=W)

        txt_name=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_name.grid(row=2,column=1,pady=10)

        # D_Head

        lbl_head=Label(Upper_frame,text='D_Head',font=('arial',15,'bold'),bg='white')
        lbl_head.grid(row=3,column=0,pady=10,sticky=W)

        txt_head=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_head.grid(row=3,column=1,pady=10)


        # D_Location

        lbl_location=Label(Upper_frame,text='D_Location',font=('arial',15,'bold'),bg='white')
        lbl_location.grid(row=4,column=0,pady=10)

        txt_location=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_location.grid(row=4,column=1,pady=10)

        




        # Button Frame
        button_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=900,y=75,width=325,height=250)

        btn_add =Button(button_frame,text='Save',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=5,pady=8)

        btn_update =Button(button_frame,text='Update',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=5,pady=8)

        btn_delete =Button(button_frame,text='Delete',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=5,pady=8)

        btn_clear =Button(button_frame,text='Clear',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=5,pady=8)


        #Back Button

        back_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        back_frame.place(x=0,y=0,width=120,height=45)
        
        btn_back =Button(back_frame,text='Back',font=('arial',15,'bold'),width=8,bg='green',fg='white')
        btn_back.grid(row=0,column=1,padx=5,)

        image_1=Image.open('MainFrame_Images/dep1.jpeg')
        image_1=image_1.resize((500,250),Image.ANTIALIAS)
        self.photo_1=ImageTk.PhotoImage(image_1)

        self.im1=Label(Upper_frame,image=self.photo_1)
        self.im1.place(x=370,y=5,width=500,height=250)



        # Down frame

        Down_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Department Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=300)

        # Search Frame

        search_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Search Department Details',font=('times new roman',15,'bold'))
        search_frame.place(x=20,y=375,width=1220,height=70)

        searchby=Label(search_frame,font=('arial',17,'bold'),text='Search By',fg='black',bg='yellow')
        searchby.grid(row=0,column=0,padx=5)

        combo_search=ttk.Combobox(search_frame,font=('arial',15,'bold'),width=17,state='readonly')
        combo_search['value']=('Select','Id','Name')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        txt_search=ttk.Entry(search_frame,width=22,font=('arial',15,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search =Button(search_frame,text='Search',font=('arial',12,'bold'),width=10,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall =Button(search_frame,text='Show All',font=('arial',12,'bold'),width=10,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)

         # --------------------------Dept table---------------------------------

        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=80,width=1225,height=180)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        





if __name__=="__main__":
    root=Tk()
    obj=Department(root)
    root.mainloop()