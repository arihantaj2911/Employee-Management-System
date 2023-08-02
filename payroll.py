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
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk

class Payroll:
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

        Upper_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Payroll',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)



          # Lable and Entry fields

         #E_id

        lbl_eid=Label(Upper_frame,text='E_ID',font=('arial',15,'bold'),bg='white')
        lbl_eid.grid(row=0,column=0,pady=10,sticky=W)

        txt_eid=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_eid.grid(row=0,column=1,pady=10)

        #P_id

        lbl_pid=Label(Upper_frame,text='P_ID',font=('arial',15,'bold'),bg='white')
        lbl_pid.grid(row=1,column=0,pady=10,sticky=W)

        txt_pid=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_pid.grid(row=1,column=1,pady=10)

        #P_Date

        lbl_pdate=Label(Upper_frame,text='P_date',font=('arial',15,'bold'),bg='white')
        lbl_pdate.grid(row=2,column=0,pady=10,sticky=W)

        txt_pdate=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_pdate.grid(row=2,column=1,pady=10)


        #P_type

        lbl_P_type=Label(Upper_frame,text='P_type',font=('arial',15,'bold'),bg='white')
        lbl_P_type.grid(row=3,column=0,pady=10,sticky=W)

        combo_P_typelbl_P_type=ttk.Combobox(Upper_frame,textvariable=self,font=('arial',15,'bold'),width=17,state='readonly')
        combo_P_typelbl_P_type['value']=('Select','Cheque','RTGS','Direct Debit')
        combo_P_typelbl_P_type.current(0)
        combo_P_typelbl_P_type.grid(row=3,column=1,pady=10)


        #P_Acc no

        lbl_accNO=Label(Upper_frame,text='Acc Number',font=('arial',15,'bold'),bg='white')
        lbl_accNO.grid(row=4,column=0,pady=10,sticky=W)

        txt_accNO=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_accNO.grid(row=4,column=1,pady=10)


        #P_Ammount

        lbl_accNO=Label(Upper_frame,text='Ammount',font=('arial',15,'bold'),bg='white')
        lbl_accNO.grid(row=0,column=2,pady=10,sticky=W,padx=20)

        txt_accNO=ttk.Entry(Upper_frame,width=22,font=('arial',15,'bold'))
        txt_accNO.grid(row=0,column=3,pady=10)


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
        
        btn_back =Button(back_frame,text='Back',command=self.back,font=('arial',15,'bold'),width=8,bg='green',fg='white')
        btn_back.grid(row=0,column=1,padx=5,)



        # Down frame

        Down_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Payroll Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=300)


        # Search Frame

        search_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Search Payroll Details',font=('times new roman',15,'bold'))
        search_frame.place(x=20,y=375,width=1220,height=70)

        searchby=Label(search_frame,font=('arial',17,'bold'),text='Search By',fg='black',bg='yellow')
        searchby.grid(row=0,column=0,padx=5)

        combo_search=ttk.Combobox(search_frame,font=('arial',15,'bold'),width=17,state='readonly')
        combo_search['value']=('Select','P_Id','Ammount')
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














    #back
    def back(self):
        self.root.destroy()







if __name__=="__main__":
    root=Tk()
    obj=Payroll(root)
    root.mainloop()