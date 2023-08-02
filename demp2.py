from cmd import IDENTCHARS
from struct import pack
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk
from pymongo import MongoClient

from employee import Employee


class Employ:

    MONGO_URI = 'mongodb://localhost:27017'

    def __init__(self, window):


    

        # db conect
        self.run_db()
       

        # window
        self.wind = window
        self.wind.geometry("1420x720+0+0")
        self.wind.title('Employee Management System - made by Shreyash')

        lbl_title=Label(self.wind,text="     EMPLOYEE MANAGEMENT SYSTEM",font=('times new roman',35,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1300,height=45)

        image_logo=Image.open('jspm.ico.png')
        image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(image_logo)

        self.logo=Label(self.wind,image=self.photo_logo)
        self.logo.place(x=200,y=0,width=50,height=50)


        #Main frame
        Main_frame=Frame(self.wind,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=46,width=1250,height=600)

        #Back Button

        back_frame=Frame(self.wind,bd=2,relief=RIDGE,bg='white')
        back_frame.place(x=0,y=0,width=120,height=45)
        
        btn_back =Button(back_frame,text='Back',command=self.back,font=('arial',15,'bold'),width=8,bg='green',fg='white')
        btn_back.grid(row=0,column=1,padx=5,)



        # Upper Frame
        Upper_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Employee',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)


        # ID Input
        Label(Upper_frame, text='ID: ',font=('arial',15,'bold'),bg='white').grid(row=1, column=0,padx=5,pady=10,sticky=W)
        self.id = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.id.focus()
        self.id.grid(row=1, column=1,pady=10)


        # Name Input
        Label(Upper_frame, text='Name: ',font=('arial',15,'bold'),bg='white').grid(row=2, column=0,padx=5,pady=10,sticky=W)
        self.name = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.name.focus()
        self.name.grid(row=2, column=1,pady=10)


        # Gender Input
        Label(Upper_frame, text='Gender: ',font=('arial',15,'bold'),bg='white').grid(row=3, column=0,padx=5,pady=10,sticky=W)
        self.gender = ttk.Combobox(Upper_frame,font=('arial',15),width=20,state='readonly')
        self.gender['value']=('Select','Male','Female','Trans Gender')
        self.gender.focus()
        self.gender.grid(row=3, column=1,pady=10)


        # City Input
        Label(Upper_frame, text='City: ',font=('arial',15,'bold'),bg='white').grid(row=4, column=0,padx=5,pady=10,sticky=W)
        self.city = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.city.focus()
        self.city.grid(row=4, column=1,pady=10)

        # DOJ Input
        Label(Upper_frame, text='DOJ: ',font=('arial',15,'bold'),bg='white').grid(row=5, column=0,padx=5,pady=10,sticky=W)
        self.doj = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.doj.focus()
        self.doj.grid(row=5, column=1,pady=10)


        # designation Input
        Label(Upper_frame, text='Designation: ',font=('arial',15,'bold'),bg='white').grid(row=1, column=2,padx=20,pady=10)
        self.designation = ttk.Combobox(Upper_frame,font=('arial',15),width=20,state='readonly')
        self.designation['value']=('Select','Intern','level 1','level 2','Team lead','Manager')
        self.designation.focus()
        self.designation.grid(row=1, column=3,pady=10)


        # salary Input
        Label(Upper_frame, text='Salary: ',font=('arial',15,'bold'),bg='white').grid(row=2, column=2,padx=20,pady=10)
        self.salary = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.salary.focus()
        self.salary.grid(row=2, column=3,pady=10)

        # mobile Input
        Label(Upper_frame, text='Contact Number: ',font=('arial',15,'bold'),bg='white').grid(row=3, column=2,padx=20,pady=10)
        self.mobile = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.mobile.focus()
        self.mobile.grid(row=3, column=3,pady=10)

        # Email Id Input
        Label(Upper_frame, text='Email Id: ',font=('arial',15,'bold'),bg='white').grid(row=4, column=2,padx=20,pady=10)
        self.email = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.email.focus()
        self.email.grid(row=4, column=3,pady=10)

        # Button Frame
        button_frame=Frame(self.wind,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=900,y=75,width=325,height=250)

        btn_add =Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=5,pady=8)

        btn_update =Button(button_frame,text='Update',command=self.edit_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=5,pady=8)

        btn_delete =Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=5,pady=8)

        btn_clear =Button(button_frame,text='Clear',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=5,pady=8)

        # Down frame
        Down_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Employee Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=290)


        # Output Messages
        self.message = LabelFrame(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)


        
        # Table Frame
        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=20,width=1225,height=200)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('id','name','gender','city','doj','designation','salary','mobile','email'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)

        self.employee_table.heading('id',text="ID")
        self.employee_table.heading('name',text="Name")
        self.employee_table.heading('gender',text="Gender")
        self.employee_table.heading('city',text="City")
        self.employee_table.heading('doj',text="DOJ")
        
        self.employee_table.heading('designation',text="Designation")
        self.employee_table.heading('salary',text="Salary")
        self.employee_table.heading('mobile',text="Contact Number")
        self.employee_table.heading('email',text="Email ID")

        self.employee_table['show']='headings'


        self.employee_table.column('id',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('city',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('designation',width=100)
        self.employee_table.column('salary',width=100)
        self.employee_table.column('mobile',width=100)
        self.employee_table.column('email',width=100)


        self.employee_table.pack(fill=BOTH,expand=1)


        # Filling the Rows
        self.get_data()

    def run_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['Employee_Management_Syst']
        self.collection = db['Employee']


    def get_data(self):
        # cleaning table
        records = self.employee_table.get_children()
        for element in records:
            self.employee_table.delete(element)
        # get products
        results = self.collection.find().sort('ID', - 1)
        # filling data
        for i in results:
            self.employee_table.insert('', 0,values=[i['id'],i['name'],i['gender'],i['city'],i['doj'],i['designation'],i['salary'],i['mobile'],i['email']])
            


    def validation(self):
        if len(self.id.get()) == 0 :
             messagebox.showinfo('Error','Enter correct Id',parent=self.wind)
        elif len(self.name.get()) == 0:
            messagebox.showinfo('Error','Enter correct Name',parent=self.wind)
        elif (self.name.get().isdigit()):
            messagebox.showinfo('Error','Enter correct Name',parent=self.wind)
        elif (self.name.get().isalpha()):
            return True
        elif (self.city.get().isdigit):
             messagebox.showinfo('Error','Enter correct City',parent=self.wind)

        elif (self.doj.get().isalpha):
            messagebox.showinfo('Error','Enter correct Date',parent=self.wind)

        elif len(self.salary.get()) == 0:
            messagebox.showinfo('Error','Enter correct Salary',parent=self.wind)
            
        elif (self.city.get().isalpha):
            return True

        elif (self.salary.get().isdigit):
            return True

        
            

            
            




            

    def add_data(self):
        if self.validation():
            self.collection.insert_one(
                {'id': self.id.get(), 'name': self.name.get(), 'gender': self.gender.get(), 'city': self.city.get(), 'doj': self.doj.get(), 'designation': self.designation.get(), 'salary':self.salary.get(), 'mobile': self.mobile.get(), 'email': self.email.get()})
            self.message['text'] = 'Product {} added Successfully'.format(
                self.name.get())
            self.id.delete(0, END)
            self.name.delete(0, END)
            self.gender.delete(0,END)
            self.city.delete(0,END)
            self.doj.delete(0,END)
            self.designation.delete(0,END)
            self.salary.delete(0,END)
            self.mobile.delete(0,END)
            self.email.delete(0,END)
            messagebox.showinfo('Success','Employee Added Successfully',parent=self.wind)
        else:
            self.message['text'] = 'Name and Price is Required'
        self.get_data()


    def delete_data(self):
        self.message['text'] = ''
        try:
            self.employee_table.delete(self.employee_table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        id = self.employee_table.item(self.employee_table.selection())['text']
        self.collection.delete_one({'id':id})
        
        self.message['text'] = 'Record {} deleted Successfully'.format(id)
        messagebox.showinfo('Success','Employee Deleted Successfully',parent=self.wind)
        self.get_data()



    def edit_data(self):
        self.message['text'] = ''
        try:
            self.employee_table.item(self.employee_table.selection())['values'][1]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.employee_table.item(self.employee_table.selection())['text']
        # Create new window
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Employee Details'

        
        old_name = self.employee_table.item(self.employee_table.selection())['values'][1]
        id = self.employee_table.item(self.employee_table.selection())['values'][0]
        old_city = self.employee_table.item(self.employee_table.selection())['values'][3]
        old_designation = self.employee_table.item(self.employee_table.selection())['values'][5]
        old_salary = self.employee_table.item(self.employee_table.selection())['values'][6]


        # id
        Label(self.edit_wind, text='ID:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=id), state='readonly').grid(row=0, column=2)

        # Old Name
        Label(self.edit_wind, text='Old Name:').grid(row=1, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_name), state='readonly').grid(row=1, column=2)
        
        # New Name
        Label(self.edit_wind, text='New Name:').grid(row=2, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=2, column=2)

        # Old City
        Label(self.edit_wind, text='Old CIty:').grid(row=1, column=4)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_city), state='readonly').grid(row=1, column=5)

         # New City
        Label(self.edit_wind, text='New City:').grid(row=2, column=4)
        new_city = Entry(self.edit_wind)
        new_city.grid(row=2, column=5)

        # Old Designation
        Label(self.edit_wind, text='Old Designation:').grid(row=3, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_designation), state='readonly').grid(row=3, column=2)

         # New Designation
        Label(self.edit_wind, text='New Designation:').grid(row=4, column=1)
        new_designation = Entry(self.edit_wind)
        new_designation.grid(row=4, column=2)

        # Old Salary
        Label(self.edit_wind, text='Old Salary:').grid(row=3, column=4)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_salary), state='readonly').grid(row=3, column=5)

         # New Salary
        Label(self.edit_wind, text='New Salary:').grid(row=4, column=4)
        new_salary = Entry(self.edit_wind)
        new_salary.grid(row=4, column=5)

        

        print(name)

        Button(self.edit_wind, text='Update', command=lambda: self.edit_records(
            new_name.get(),old_name , new_city.get(),old_city , new_designation.get(),old_designation , new_salary.get(),old_salary)).grid(row=10, column=3, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, old_name , old_city ,new_city , old_designation , new_designation , old_salary , new_salary):
        print(old_name)
        print(old_city)
        print(old_designation)
        print(old_salary)
        self.collection.update_one(
            {'name': old_name}, {'$set': {'name': new_name , 'city': new_city , 'designation':new_designation , 'salary':new_salary}})
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(old_name,old_city,old_designation,old_salary)
        self.get_data()



    
        












        




    
            
    



    #back
    def back(self):
        self.wind.destroy()



if __name__ == '__main__':
    window = Tk()
    application = Employ(window)
    window.mainloop()