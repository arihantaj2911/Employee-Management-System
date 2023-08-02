from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import bgcolor
from unittest import result
import pymongo
from pymongo import collection
root=Tk()
root.geometry("1500x900")
root.title("Employee_Management_System | Arihant")

e_idv = StringVar()
e_Namev = StringVar()
e_Mob_v = StringVar()
e_Salaryv = StringVar()
e_Designationv = StringVar()
e_DOJv= StringVar()
e_DOJv= StringVar()
e_ID_PROOFv = StringVar()
e_Emailv= StringVar()
checkvalue = IntVar

def getvals():
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['Employee_Management_SYS']
    collection=db["Empl"]
    dic={
        'E_id':e_idv.get(),
        'E_name': e_Namev.get(),
        'E_mob': e_Mob_v.get(),
        'E_Designation':e_Designationv.get(),
        'E_Salary': e_Salaryv.get(),
        'E_DOJ': e_DOJv.get(),
        'E_ID_PROOF':e_ID_PROOFv.get(),
        'E_Email':e_Emailv.get()
    }  
        
    collection.insert_one(dic)
    messagebox.showinfo('Success','Employee Added Successfully',parent=root)

    # print("ACCEPTED")

#Label(root, text="                          EMPLOYEE MANAGEMENT SYSTEM      ", font="arial 26 bold",bg="red",fg="white").place(x=10,y=10)
title=Label(root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="red",fg="white").place(x=5,y=5,relwidth=1)


Frame1=Frame(root,bd=5,relief=RIDGE,bg="white")
Frame1.place(x=3,y=70,width=1100,height=435)

title=Label(Frame1,text="Employee Details",font=("times new roman",25,"bold"),bg="grey",fg="black")
title.place(x=0,y=0,relwidth=1)

e_id=Label(Frame1,text="Id",font=("times new roman",20,'bold'),bg="white",fg="black")
e_id.place(x=20,y=70)
e_id=Entry(Frame1,font=("times new roman",16),text=e_idv,bg="light blue",fg="black").place(x=240,y=75,width=160,height=30)


e_name=Label(Frame1,text="Name",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=600,y=70)
e_name=Entry(Frame1,font=("times new roman",16),text=e_Namev,bg="light blue",fg="black").place(x=880,y=75,width=180,height=30)

e_Mob=Label(Frame1,text="Mob",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=20,y=150)
e_mob=Entry(Frame1,font=("times new roman",16),text=e_Mob_v,bg="light blue",fg="black").place(x=240,y=155,width=160,height=30)

e_Designation=Label(Frame1,text="Designation",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=600,y=150)
e_Designation=Entry(Frame1,font=("times new roman",16),text=e_Designationv,bg="light blue",fg="black").place(x=880,y=155,width=180,height=30)

e_Salary=Label(Frame1,text="Salary",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=20,y=230)
e_Salary=Entry(Frame1,font=("times new roman",16),text=e_Salaryv,bg="light blue",fg="black").place(x=240,y=235,width=160,height=30)

e_DOJ=Label(Frame1,text="DOJ",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=600,y=230)
e_DOJ=Entry(Frame1,font=("times new roman",16),text=e_DOJv,bg="light blue",fg="black").place(x=880,y=235,width=180)

e_ID_PROOF=Label(Frame1,text="ID_PROOF",font=("times new roman",19,'bold'),bg="white",fg="black").place(x=20,y=310)
e_ID_PROOF=Entry(Frame1,font=("times new roman",16),text=e_ID_PROOFv,bg="light blue",fg="black").place(x=240,y=315,width=160,height=30)

e_EMAIL=Label(Frame1,text="Email",font=("times new roman",20,'bold'),bg="white",fg="black").place(x=600,y=310)
e_Email=Entry(Frame1,font=("times new roman",16),text=e_Emailv,bg="light blue",fg="black").place(x=880,y=315,width=180,height=30)



Frame2=Frame(root,bd=5,relief=RIDGE,bg="white")
Frame2.place(x=1105,y=73,width=390,height=435)
title_3=Label(Frame2,text="OPERATIONS",font=("times new roman",25,"bold"),bg="grey",fg="black").place(x=0,y=0,relwidth=1)

btn_Calculate=Button(Frame2,text="Calculate",font=("times new roman",23,"bold"),bg="orange",fg="black").place(x=30,y=80)
btn_Update=Button(Frame2,text="Update",font=("times new roman",25,"bold"),bg="light blue",fg="black").place(x=230,y=80)
btn_Delete=Button(Frame2,text="Delete",font=("times new roman",25,"bold"),bg="red",fg="black").place(x=35,y=200)
btn_Save=Button(Frame2,text="Save",font=("times new roman",25,"bold"),command=getvals,bg="green",fg="black").place(x=235,y=200)
btn_Search=Button(Frame2,text="Search",font=("times new roman",25,"bold"),bg="yellow",fg="black").place(x=35,y=320)
btn_Reset=Button(Frame2,text="Reset",font=("times new roman",25,"bold"),bg="grey",fg="black").place(x=235,y=320)

Frame3=Frame(root,bd=5,relief=RIDGE,bg="white")
Frame3.place(x=3,y=500,width=1490,height=320)

Frame4=Frame(root,bd=5,relief=RIDGE,bg="white")
Frame4.place(x=10,y=506,width=1475,height=308)

# def add(root):
#     if e_idv.get()==" " or e_Namev.get()==" ":
#         messagebox.showerror("Employee details are required")
#     else:
#         if Entry!=None:
#             messagebox.showerror("Error,This Employee ID is already available in our record")
#         else:
#             (
#             e_idv.get(),
#             e_Namev.get(),
#             e_Mob_v.get(),
#             e_Designationv.get(),
#             e_Salaryv.get(),
#             e_DOJv.get(),
#             e_ID_PROOFv.get(),
#             e_Emailv.get(),
#             )

def search(root):
    try:
        con=pymongo.MongoClient("mongodb://localhost:27017/")
        cur=con.cursor()
        cur.execute("db.Collection_name.find()",(e_idv.get()))
        row=cur.fetchone()
        # print(rows)
        if row==None:
            messagebox.showerror("Error","Invalid Employee ID",parent=root)
        else:
            print(row)
    except Exception as ex:
        messagebox.showerror("Error","Error due to: {str(ex)}")
            
        messagebox.showinfo("Sucess","Record Added Sucessfully")
            
            


# def check_connection(self):
#     try:
#         con=pymongo.MongoClient("mongodb://localhost:27017/")
#         cur=con.cursor()
#         cur.execute("db.Collection_name.find()")
#         rows=cur.fetchall()
#         print(rows)
#     except Exception as ex:
#         messagebox.showerror("Error",f"Error due to: {str(ex)}")

        





        







root.mainloop()


