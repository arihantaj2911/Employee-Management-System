
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk
from pymongo import MongoClient

from employee import Employee


class dept:

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
        Upper_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Department',font=('times new roman',18,'bold'),fg='red')
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

        # D_Head Input
        Label(Upper_frame, text='D_Head: ',font=('arial',15,'bold'),bg='white').grid(row=3, column=0,padx=5,pady=10,sticky=W)
        self.head = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.head.focus()
        self.head.grid(row=3, column=1,pady=10)

        # D_Location Input
        Label(Upper_frame, text='D_Location: ',font=('arial',15,'bold'),bg='white').grid(row=4, column=0,padx=5,pady=10,sticky=W)
        self.location = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.location.focus()
        self.location.grid(row=4, column=1,pady=10)


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

        # Images
        image_1=Image.open('MainFrame_Images/dep1.jpeg')
        image_1=image_1.resize((500,250),Image.ANTIALIAS)
        self.photo_1=ImageTk.PhotoImage(image_1)

        self.im1=Label(Upper_frame,image=self.photo_1)
        self.im1.place(x=370,y=5,width=500,height=250)

        # Down frame
        Down_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Department Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=290)


        # Output Messages
        self.message = LabelFrame(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)


        
        # Table Frame
        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=20,width=1225,height=200)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.department_table=ttk.Treeview(table_frame,column=('id','name','head','location'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.department_table.xview)
        scrolly.config(command=self.department_table.yview)

        self.department_table.heading('id',text="ID")
        self.department_table.heading('name',text="Name")
        self.department_table.heading('head',text="D_Head")
        self.department_table.heading('location',text="D_Location")

        self.department_table['show']='headings'

        self.department_table.column('id',width=100)
        self.department_table.column('name',width=100)
        self.department_table.column('head',width=100)
        self.department_table.column('location',width=100)

        self.department_table.pack(fill=BOTH,expand=1)

        
        
        # Filling the Rows
        self.get_data()


    def run_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['Employee_Management_Syst']
        self.collection = db['Department']


    def get_data(self):
        # cleaning table
        records = self.department_table.get_children()
        for element in records:
            self.department_table.delete(element)
        # get products
        results = self.collection.find().sort('ID', - 1)
        # filling data
        for i in results:
            self.department_table.insert('', 0,values=[i['id'],i['name'],i['head'],i['location']])


    def validation(self):
        #match = re.match("([a-z]+)( [a-z]+)*( [a-z]+)*$", self.name.get())

        if len(self.id.get()) == 0:
            messagebox.showinfo('Error','Enter correct Id',parent=self.wind)
            return False
        elif(self.id.get().isdigit()):
            messagebox.showinfo('Error','Invalid ID',parent=self.wind)
            
        elif len(self.name.get()) == 0:
            messagebox.showinfo('Error','Enter correct Name',parent=self.wind)
            return False
        elif len(self.head.get()) == 0:
            messagebox.showinfo('Error','Enter correct Head',parent=self.wind)
            return False
        elif len(self.location.get()) == 0:
            messagebox.showinfo('Error','Enter correct Location',parent=self.wind)
            return False
        elif(self.name.get().isdigit()):
            messagebox.showinfo('Error','Invalid name',parent=self.wind)
            return False
        elif(self.head.get().isdigit()):
            messagebox.showinfo('Error','Invalid Head',parent=self.wind)
            return False
        elif(self.location.get().isdigit()):
            messagebox.showinfo('Error','Invalid Location',parent=self.wind)
            return False
        else:
            return True

            '''if match is not None :
            messagebox.showinfo('Error','Invalid Name',parent=self.wind)
            return False'''
        
        # elif (self.head.get().isdigit):
        #     messagebox.showinfo('Error','Enter correct Head',parent=self.wind)
        # elif (self.location.get().isdigit):
        #     messagebox.showinfo('Error','Enter correct Location',parent=self.wind)

        '([a-z]+)( [a-z]+)*( [a-z]+)*$'
        


        # # elif (self.name.get().isdigit):
        # #     messagebox.showinfo('Error','Enter correct Name',parent=self.wind)    
       

        # elif (self.head.get()) == 0:
        #     messagebox.showinfo('Error','Enter correct value',parent=self.wind)
        # # elif (self.head.get().isdigit):
        # #     messagebox.showinfo('Error','Enter correct value',parent=self.wind)  
        # elif (self.head.get().isalpha) and (self.name.get().isalpha()):
        #     return True     
        



     
    def add_data(self):
        if self.validation():
            self.collection.insert_one(
                {'id': self.id.get(), 'name': self.name.get(), 'head': self.head.get(), 'location': self.location.get()})
            self.message['text'] = 'Product {} added Successfully'.format(
                self.name.get())
            self.id.delete(0, END)
            self.name.delete(0, END)
            self.head.delete(0,END)
            self.location.delete(0,END)
        else:
            self.message['text'] = 'Name and Price is Required'
        self.get_data()




    def delete_data(self):
        self.message['text'] = ''
        try:
            self.department_table.delete(self.department_table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        id = self.department_table.item(self.department_table.selection())['text']
        self.collection.delete_one({'id':id})
        self.message['text'] = 'Record {} deleted Successfully'.format(id)
        self.get_data()


    

    def edit_data(self):
        self.message['text'] = ''
        try:
            self.department_table.item(self.department_table.selection())['values'][1]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.department_table.item(self.department_table.selection())['text']
        # Create new window
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Department Details'

        
        old_name = self.department_table.item(self.department_table.selection())['values'][1]
        id = self.department_table.item(self.department_table.selection())['values'][0]
        old_city = self.department_table.item(self.department_table.selection())['values'][2]
        old_designation = self.department_table.item(self.department_table.selection())['values'][3]
       


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
        Label(self.edit_wind, text='Old Head:').grid(row=1, column=4)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_city), state='readonly').grid(row=1, column=5)

         # New City
        Label(self.edit_wind, text='New Head:').grid(row=2, column=4)
        new_city = Entry(self.edit_wind)
        new_city.grid(row=2, column=5)

        # Old Designation
        Label(self.edit_wind, text='Old Location:').grid(row=3, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
              value=old_designation), state='readonly').grid(row=3, column=2)

         # New Designation
        Label(self.edit_wind, text='New Location:').grid(row=4, column=1)
        new_designation = Entry(self.edit_wind)
        new_designation.grid(row=4, column=2)


        

        print(name)

        Button(self.edit_wind, text='Update', command=lambda: self.edit_records(
            new_name.get(),old_name , new_city.get(),old_city , new_designation.get(),old_designation )).grid(row=10, column=3, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, old_name , old_city ,new_city , old_designation , new_designation):
        print(old_name)
        print(old_city)
        print(old_designation)
        self.collection.update_one(
            {'name': old_name}, {'$set': {'name': new_name , 'city': new_city , 'designation':new_designation}})
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(old_name,old_city,old_designation)
        self.get_data()


    



        


















     #back
    def back(self):
        self.wind.destroy()




if __name__ == '__main__':
    window = Tk()
    application = dept(window)
    window.mainloop()
