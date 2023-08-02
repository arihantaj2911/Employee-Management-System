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

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1420x720+0+0")
        self.root.title("Employee Management System - made by Shreyash")

        self.run_db


        # Variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_mobileno=StringVar()
        self.var_city=StringVar()
        self.var_salary=StringVar()
        self.var_desig=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()


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

        Upper_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Employee',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)


         # Lable and Entry fields

         #id

        lbl_empid=Label(Upper_frame,text='  ID',font=('arial',15,'bold'),bg='white')
        lbl_empid.grid(row=0,column=0,pady=10,sticky=W)

        txt_empid=ttk.Entry(Upper_frame,textvariable=self.var_id,width=22,font=('arial',15,'bold'))
        txt_empid.grid(row=0,column=1,pady=10)


        # name

        lbl_name=Label(Upper_frame,text='Name',font=('arial',15,'bold'),bg='white')
        lbl_name.grid(row=2,column=0,pady=10)

        txt_name=ttk.Entry(Upper_frame,textvariable=self.var_name,width=22,font=('arial',15,'bold'))
        txt_name.grid(row=2,column=1,pady=10)


        # Gender

        lbl_gender=Label(Upper_frame,text='Gender',font=('arial',15,'bold'),bg='white')
        lbl_gender.grid(row=3,column=0,pady=10)

        combo_genderlbl_gender=ttk.Combobox(Upper_frame,textvariable=self.var_gender,font=('arial',15,'bold'),width=17,state='readonly')
        combo_genderlbl_gender['value']=('Select','Male','Female','Trans Gender')
        combo_genderlbl_gender.current(0)
        combo_genderlbl_gender.grid(row=3,column=1,pady=10)

        # Mobile No

        lbl_nobileno=Label(Upper_frame,text=' Contact Number',font=('arial',15,'bold'),bg='white')
        lbl_nobileno.grid(row=3,column=3,pady=10,padx=50)

        txt_nobileno=ttk.Entry(Upper_frame,textvariable=self.var_mobileno,width=22,font=('arial',15,'bold'))
        txt_nobileno.grid(row=3,column=4,pady=10)

        # Address

        lbl_ecity=Label(Upper_frame,text='  City',font=('arial',15,'bold'),bg='white')
        lbl_ecity.grid(row=4,column=0,pady=10,sticky=W)

        txt_ecity=ttk.Entry(Upper_frame,textvariable=self.var_city,width=22,font=('arial',15,'bold'))
        txt_ecity.grid(row=4,column=1,pady=10)

        # Salary

        lbl_salary=Label(Upper_frame,text='Salary',font=('arial',15,'bold'),bg='white')
        lbl_salary.grid(row=2,column=3,pady=10,padx=50)

        txt_salary=ttk.Entry(Upper_frame,textvariable=self.var_salary,width=22,font=('arial',15,'bold'))
        txt_salary.grid(row=2,column=4,pady=10)

        # Designation

        lbl_designation=Label(Upper_frame,text='   Designation',font=('arial',15,'bold'),bg='white')
        lbl_designation.grid(row=0,column=3,padx=50,pady=10,sticky=W)

        combo_designation=ttk.Combobox(Upper_frame,textvariable=self.var_desig,font=('arial',15,'bold'),width=17,state='readonly')
        combo_designation['value']=('Select','Intern','level 1','level 2','Team lead','Manager')
        combo_designation.current(0)
        combo_designation.grid(row=0,column=4,pady=10)

        # DOJ

        lbl_doj=Label(Upper_frame,text='DOJ',font=('arial',15,'bold'),bg='white')
        lbl_doj.grid(row=5,column=0,pady=10)

        txt_doj=ttk.Entry(Upper_frame,textvariable=self.var_doj,width=22,font=('arial',15,'bold'))
        txt_doj.grid(row=5,column=1,pady=10)


        

        # Email

        lbl_email=Label(Upper_frame,text='Email ID',font=('arial',15,'bold'),bg='white')
        lbl_email.grid(row=4,column=3,pady=10,padx=50)

        txt_email=ttk.Entry(Upper_frame,textvariable=self.var_email,width=22,font=('arial',15,'bold'))
        txt_email.grid(row=4,column=4,pady=10)


        # Button Frame
        button_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=900,y=75,width=325,height=250)

        btn_add =Button(button_frame,text='Save',command=self.AddData,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=5,pady=5)

        btn_update =Button(button_frame,text='Update',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=5,pady=5)

        btn_delete =Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=5,pady=5)

        btn_clear =Button(button_frame,text='Clear',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=5,pady=5)

             
                #Back Button

        back_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        back_frame.place(x=0,y=0,width=120,height=45)
        
        btn_back =Button(back_frame,text='Back',command=self.back,font=('arial',15,'bold'),width=8,bg='green',fg='white')
        btn_back.grid(row=0,column=1,padx=5,)


        # Down frame

        Down_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Employee Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=300)

        # Search Frame

        search_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg='white',text='Search Employee Details',font=('times new roman',15,'bold'))
        search_frame.place(x=20,y=375,width=1220,height=70)

        searchby=Label(search_frame,font=('arial',17,'bold'),text='Search By',fg='black',bg='yellow')
        searchby.grid(row=0,column=0,padx=5)

        combo_search=ttk.Combobox(search_frame,font=('arial',15,'bold'),width=17,state='readonly')
        combo_search['value']=('Select','Employee Id','Employee Name','Salary','DOJ')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        txt_search=ttk.Entry(search_frame,width=22,font=('arial',15,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search =Button(search_frame,text='Search',font=('arial',12,'bold'),width=10,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall =Button(search_frame,text='Show All',font=('arial',12,'bold'),width=10,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=0, column=5)



        # --------------------------Employee table---------------------------------

        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=80,width=1225,height=180)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('id','name','mob','city','sal','desig','doj','gender','email'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)



        self.employee_table.heading('id',text="Employee ID")
        self.employee_table.heading('mob',text="Mobile Number")
        self.employee_table.heading('name',text="Employee Name")
        self.employee_table.heading('city',text="Employee City")
        self.employee_table.heading('sal',text="Salary")
        self.employee_table.heading('desig',text="Designation")
        self.employee_table.heading('doj',text="DOJ")
        self.employee_table.heading('gender',text="Gender")
        self.employee_table.heading('email',text="Email ID")

        self.employee_table['show']='headings'

        self.employee_table.column('id',width=100)
        self.employee_table.column('mob',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('city',width=100)
        self.employee_table.column('sal',width=100)
        self.employee_table.column('desig',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('email',width=100)

        self.employee_table.bind("<ButtonRelease>",self.getcursor)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.Fetch_data()

    
    #------------------Function Decleration------------------------

    def run_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['Employee_Management_System']
        self.collection = db['Employee']

    

    def AddData(self):
        client=pymongo.MongoClient("mongodb://localhost:27017")
        db=client['Employee_Management_System']
        collection=db['Employee']
        dic={
            'Employee Id':self.var_id.get(),
            'Employee Name':self.var_name.get(),
            'Mobile Number':self.var_mobileno.get(),
            'Employee City':self.var_city.get(),
            'Employee Salary':self.var_salary.get(),
            'Designation':self.var_desig.get(),
            'DOJ':self.var_doj.get(),
            'Gender':self.var_gender.get(),
            'Email ID':self.var_email.get()

        }
        collection.insert_one(dic)
        messagebox.showinfo('Success','Employee Added Successfully',parent=self.root)
        self.Fetch_data


        # Fetch Data
    def Fetch_data(self):
        client=pymongo.MongoClient("mongodb://localhost:27017")
        db=client['Employee_Management_System']
        collection=db['Employee']
        data=collection.find().sort('Employee Id', -1)
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
            self.employee_table.insert("",END,values=[i['Employee Id'],i['Employee Name'],i['Mobile Number'],i['Employee City'],i['Employee Salary'],i['Designation'],i['DOJ'],i['Gender'],i['Email ID']])
            

    def getcursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_id.set(data[0]) 
        self.var_name.set(data[1])
        self.var_mobileno.set(data[2]) 
        self.var_city.set(data[3])
        self.var_salary.set(data[4]) 
        self.var_desig.set(data[5])
        self.var_doj.set(data[6]) 
        self.var_gender.set(data[7])
        self.var_email.set(data[8])



    def update_data(self):
        
            client=pymongo.MongoClient("mongodb://localhost:27017")
            db=client['Employee_Management_System']
            collection=db['Employee']
            collection.update_one

    def delete_data(self):
        self.message['text'] = ''
        try:
            self.employee_table.item(self.employee_table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        id = self.employee_table.item(self.employee_table.selection())['text']
        self.collection.delete_one({'ID':self.var_id})
        self.message['text'] = 'Record {} deleted Successfully'.format(id)
        self.Fetch_data()
            
        
    #back
    def back(self):
        self.root.destroy()



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
