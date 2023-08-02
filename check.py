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
from socket import fromfd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk
from employee import Employee
from department import Department
from payroll import Payroll

class Main:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1420x720+0+0")
                self.root.title("Employee Management System - made by Shreyash")

                lbl_title=Label(self.root,text="     EMPLOYEE MANAGEMENT SYSTEM",font=('times new roman',35,'bold'),fg='darkblue',bg='white')
                lbl_title.place(x=0,y=0,width=1300,height=45)

                #image_logo=Image.open('jspm.ico.png')
                #image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
                #self.photo_logo=ImageTk.PhotoImage(image_logo)

                #self.logo=Label(self.root,image=self.photo_logo)
                #self.logo.place(x=200,y=0,width=50,height=50)

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
                # image_1=Image.open('MainFrame_Images/b.jpg')
                # image_1=image_1.resize((400,200),Image.ANTIALIAS)
                # self.photo_1=ImageTk.PhotoImage(image_1)

                # self.im1=Label(Main_frame,image=self.photo_1)
                # self.im1.place(x=0,y=5,width=400,height=220)

                # image_2=Image.open('MainFrame_Images/c.jpg')
                # image_2=image_2.resize((500,200),Image.ANTIALIAS)
                # self.photo_2=ImageTk.PhotoImage(image_2)

                # self.im2=Label(Main_frame,image=self.photo_2)
                # self.im2.place(x=402,y=5,width=500,height=220)

                # image_3=Image.open('MainFrame_Images/a.jpeg')
                # image_3=image_3.resize((400,200),Image.ANTIALIAS)
                # self.photo_3=ImageTk.PhotoImage(image_3)

                # self.im3=Label(Main_frame,image=self.photo_3)
                # self.im3.place(x=904,y=5,width=400,height=220)


# Entities

                entities=Label(left_frame,font=('arial',17,'bold'),text='Entities :-',fg='red',bg='white')
                entities.place(x=0,y=0)

        #1

                # emp=Image.open('MainFrame_Images/OIP.jpg')
                # emp=emp.resize((250,100),Image.ANTIALIAS)
                # self.photo_4=ImageTk.PhotoImage(emp)

                # self.img1=Label(left_frame,image=self.photo_4)
                # self.img1.place(x=60,y=30,width=250,height=100)

                btn_employee =Button(left_frame,text='Employee',command=self.emp_details,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
                btn_employee.place(x=140,y=150,width=100,height=30)


        

                
               


                


        #2

                # dep=Image.open('MainFrame_Images/R.png')
                dep=dep.resize((250,120),Image.ANTIALIAS)
                # self.photo_5=ImageTk.PhotoImage(dep)

                # self.img2=Label(left_frame,image=self.photo_5)
                # self.img2.place(x=550,y=30,width=250,height=120)


                btn_department =Button(left_frame,text='Department',command=self.dep_details,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
                btn_department.place(x=630,y=150,width=120,height=30)

        


        


#3

        
                # pay=Image.open('MainFrame_Images/P.jpg')
                # pay=pay.resize((250,120),Image.ANTIALIAS)
                # self.photo_6=ImageTk.PhotoImage(pay)

                # self.img3=Label(left_frame,image=self.photo_6)
                # self.img3.place(x=330,y=160,width=250,height=120)

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
                self.app1=Employee(self.new_window1)


        def dep_details(self):
                self.new_window2=Toplevel(self.root)
                self.app2=Department(self.new_window2)


        def pay_details(self):
                self.new_window3=Toplevel(self.root)
                self.app3=Payroll(self.new_window3)


        def exit(self):
                self.root.destroy()







emp
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

        # image_logo=Image.open('jspm.ico.png')
        # image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(image_logo)

        # self.logo=Label(self.root,image=self.photo_logo)
        # self.logo.place(x=200,y=0,width=50,height=50)

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





dept
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
        
        btn_back =Button(back_frame,text='Back',command=self.back,font=('arial',15,'bold'),width=8,bg='green',fg='white')
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

        

    
    #back
    def back(self):
        self.root.destroy()




if __name__=="__main__":
    root=Tk()
    obj=Department(root)
    root.mainloop()


pay
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
        


















        










if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()