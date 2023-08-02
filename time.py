
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import st, width
import pymongo
from pymongo import collection
from PIL import Image,ImageTk
from pymongo import MongoClient
import time
import sys

from employee import Employee



master = Tk()


class pay:

    MONGO_URI = 'mongodb://localhost:27017'

    def __init__(self, window):

        # db conect
        self.run_db()
        self.get_time()

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
        Upper_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Payroll',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)


        

        # Upper Frame
        Upper_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Department',font=('times new roman',18,'bold'),fg='red')
        Upper_frame.place(x=14,y=48,width=1240,height=300)
        
        # E-ID Input
        Label(Upper_frame, text='E-ID: ',font=('arial',15,'bold'),bg='white').grid(row=1, column=0,padx=5,pady=10,sticky=W)
        self.E_id = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.E_id.focus()
        self.E_id.grid(row=1, column=1,pady=10)


        # P-ID Input
        Label(Upper_frame, text='P-ID: ',font=('arial',15,'bold'),bg='white').grid(row=2, column=0,padx=5,pady=10,sticky=W)
        self.P_id = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.P_id.focus()
        self.P_id.grid(row=2, column=1,pady=10)

        # P_Date Input
        Label(Upper_frame, text='P_date: ',font=('arial',15,'bold'),bg='white').grid(row=3, column=0,padx=5,pady=10,sticky=W)
        self.P_Date = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.P_Date.focus()
        self.P_Date.grid(row=3, column=1,pady=10)

        # P_Type Input
        Label(Upper_frame, text='P_Type: ',font=('arial',15,'bold'),bg='white').grid(row=4, column=0,padx=5,pady=10,sticky=W)
        self.P_type = ttk.Combobox(Upper_frame,font=('arial',15),width=20,state='readonly')
        self.P_type['value']=('Select','Cheque','RTGS','Direct Debit')
        self.P_type.focus()
        self.P_type.grid(row=4, column=1,pady=10)

        # Acc N0 Input
        Label(Upper_frame, text='ACC_No: ',font=('arial',15,'bold'),bg='white').grid(row=5, column=0,padx=5,pady=10,sticky=W)
        self.Acc_No = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.Acc_No.focus()
        self.Acc_No.grid(row=5, column=1,pady=10)

        # Ammount Input
        Label(Upper_frame, text='Ammount: ',font=('arial',15,'bold'),bg='white').grid(row=1, column=2,padx=20,pady=10,sticky=W)
        self.Ammount = Entry(Upper_frame,width=22,bg='light grey',font=('arial',15))
        self.Ammount.focus()
        self.Ammount.grid(row=1, column=3,pady=10)


        # Button Frame
        button_frame=Frame(self.wind,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=900,y=75,width=325,height=250)

        btn_add =Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=5,pady=8)

        btn_update =Button(button_frame,text='Update',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=5,pady=8)

        btn_delete =Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=5,pady=8)

        btn_clear =Button(button_frame,text='Clear',font=('arial',15,'bold'),width=25,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=5,pady=8)


         # Down frame
        Down_frame=LabelFrame(self.wind,bd=2,relief=RIDGE,bg='white',text='Payroll Table',font=('times new roman',18,'bold'),fg='red')
        Down_frame.place(x=14,y=350,width=1240,height=290)


        # Output Messages
        self.message = LabelFrame(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        
        # Table Frame
        table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=80,width=1225,height=180)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.payroll_table=ttk.Treeview(table_frame,column=('E_id','P_id','P_date','P_type','Acc_No','Ammount'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.payroll_table.xview)
        scrolly.config(command=self.payroll_table.yview)


        self.payroll_table.heading('E_id',text="E_ID")
        self.payroll_table.heading('P_id',text="P_ID")
        self.payroll_table.heading('P_date',text="P_Date")
        self.payroll_table.heading('P_type',text="P_Type")
        self.payroll_table.heading('Acc_No',text="Acc_no")
        self.payroll_table.heading('Ammount',text="Ammount")

        self.payroll_table['show']='headings'


        self.payroll_table.column('E_id',width=100)
        self.payroll_table.column('P_id',width=100)
        self.payroll_table.column('P_date',width=100)
        self.payroll_table.column('P_type',width=100)
        self.payroll_table.column('Acc_No',width=100)
        self.payroll_table.column('Ammount',width=100)

        self.payroll_table.pack(fill=BOTH,expand=1)



        # Filling the Rows
        self.get_data()


    def run_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['Employee_Management_Syst']
        self.collection = db['Payroll']



    def get_data(self):
        # cleaning table
        records = self.payroll_table.get_children()
        for element in records:
            self.payroll_table.delete(element)
        # get products
        results = self.collection.find().sort('ID', - 1)
        # filling data
        for i in results:
            self.payroll_table.insert('', 0,values=[i['E_id'],i['P_id'],i['P_date'],i['P_type'],i['Acc_No'],i['Ammount']])



    def validation(self):
        return len(self.E_id.get()) != 0





    def add_data(self):
        if self.validation():
            self.collection.insert_one(
                {'E_id': self.E_id.get(), 'P_id': self.P_id.get(), 'P_date': self.P_Date.get(), 'P_type': self.P_type.get(), 'Acc_No': self.Acc_No.get(), 'Ammount': self.Ammount.get()})
            self.message['text'] = 'Product {} added Successfully'.format(
                self.P_id.get())
            self.E_id.delete(0, END)
            self.P_id.delete(0, END)
            self.P_Date.delete(0,END)
            self.P_type.delete(0,END)
            self.Acc_No.delete(0,END)
            self.Ammount.delete(0,END)
        else:
            self.message['text'] = 'Name and Price is Required'
        self.get_data()




    def delete_data(self):
        self.message['text'] = ''
        try:
            self.payroll_table.delete(self.payroll_table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        id = self.payroll_table.item(self.payroll_table.selection())['text']
        self.collection.delete_one({'id':id})
        self.message['text'] = 'Record {} deleted Successfully'.format(id)
        self.get_data()


    def get_time(self):
        timevar = time.strftime("%I:%M:%S %p")
        clock.config(text=timevar)
        clock.after(200,self.get_time)
        self.get_time


clock = Label(master, font=("Calibri",20),bg="grey",fg="white")
clock.pack()





    














        












    # #back
    #     def back(self):
    #         self.wind.destroy()



if __name__ == '__main__':
    window = Tk()
    application = pay(window)
    window.mainloop()
