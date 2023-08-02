import pymongo
conn_str="mongodb://localhost:27017/users"
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:" + Exception)


mydb = client["pymongo_demo"]

dic={
            

        'E_id':var_Employee_id.get(),
        'Employee_name':self.var_Employee_Name.get(),
        'Employee_Mob_no':self.var_Employee_Mob_no.get(),
        'Employee_Designation':self.var_Employee_Designation.get(),
        'Employee_Salary':self.var_Employee_Salary.get(),   
        'Employee_DOJ':self.var_Employee_DOJ.get(),
        'Employee_Email': self.var_Employee_Email.get()
    }

print(client.list_database_names())


def sub(self):
    client=pymongo.MongoClient("mongodb://localhost:27017/users")
    db=client["Employee Management SYS"]
    collection=db["Employee"]

        self.var_Employee_id.get()
        self.var_Employee_Name.get()
        self.var_Employee_Mob_no.get()
        self.var_Employee_Designation.get()
        self.var_Employee_Salary.get()
        self.var_Employee_DOJ.get()
        self.var_Employee_Email.get()

        #===============frame2=================

        self.var_p_id.get()
        self.var_p_Month.get(),
        self.var_p_Date.get(),
        self.var_p_Amount.get(),
        self.var_p_Account.get(),
        self.var_Total_Days.get(),
        self.var_Absents.get(),
        self.var_PF.get(),
        self.var_Net_Salary.get(),
        self.var_p_Type.get()
    
    
    E_id= Label(root, text="     E_id", font="arial 18 bold")

E_name= Label(root, text="   E_name", font="arial 18 bold")

E_mob_no= Label(root, text="    E_mob_no", font="arial 18 bold")

E_salary= Label(root, text="   E_salary", font="arial 18 bold")

E_designation= Label(root, text="    E_designation", font="arial 18 bold")

E_joining_date= Label(root, text="   E_joining_date", font="arial 18 bold")

E_id.grid(row=2, column=2)
E_name.grid(row=8, column=2)
E_mob_no.grid(row=14, column=2)
E_salary.grid(row=20, column=2)
E_designation.grid(row=26, column=2)
E_joining_date.grid(row=32, column=2)

E_idvalue = StringVar()
E_namevalue = StringVar()
E_mob_novalue = StringVar()
E_salaryvalue = StringVar()
E_designationvalue = StringVar()
E_joining_datevalue= StringVar()
checkvalue = IntVar

E_identry = Entry(root , textvariable = E_idvalue)
E_nameentry = Entry(root , textvariable = E_namevalue)
E_mob_noentry = Entry(root , textvariable = E_mob_novalue)
E_salaryentry = Entry(root , textvariable = E_salaryvalue)
E_designationentry = Entry(root , textvariable = E_designationvalue)
E_joining_dateentry = Entry(root , textvariable = E_joining_datevalue)

E_identry.grid(row=2,column=3)
E_nameentry.grid(row=8,column=3)
E_mob_noentry.grid(row=14,column=3)
E_salaryentry.grid(row=20,column=3)
E_designationentry.grid(row=26,column=3)
E_joining_dateentry.grid(row=32,column=3)

checkbtn = Checkbutton(text="Remember me?", variable = checkvalue)
checkbtn.grid(row=34 , column =3)

Button(text="Submit", command=getvals).grid(row=36 ,column=3)




#####################################################

lbl_mob=Label(Frame1,text="Employee_Mob_no",font=("times new roman",18),bg="white",fg="black").place(x=10,y=270)
txt_mob=Entry(Frame1,font=("times new roman",16),bg="light blue",fg="black").place(x=250,y=275,width=160,height=30)

lbl_Designation=Label(Frame1,text="Employee_Designation",font=("times new roman",18),bg="white",fg="black").place(x=10,y=370)
txt_Designation=Entry(Frame1,font=("times new roman",16),bg="light blue",fg="black").place(x=250,y=370,width=160,height=30)        

lbl_salary=Label(Frame1,text="Employee_Salary",font=("times new roman",18),bg="white",fg="black").place(x=10,y=470)
txt_salary=Entry(Frame1,font=("times new roman",16),bg="light blue",fg="black").place(x=250,y=470,width=160,height=30)

lbl_DOJ=Label(Frame1,text="Employee_DOJ",font=("times new roman",18),bg="white",fg="black").place(x=10,y=570)
txt_DOJ=Entry(Frame1,font=("times new roman",16),bg="light blue",fg="black").place(x=250,y=570,width=160,height=30)

lbl_Email=Label(Frame1,text="Employee_Email",font=("times new roman",18),bg="white",fg="black").place(x=10,y=670)
txt_Email=Entry(Frame1,font=("times new roman",16),bg="light blue",fg="black").place(x=250,y=670,width=160,height=30)




#####################################################################################

def add(root):
    if e_idv.get()==" " or e_Namev.get()==" ":
        messagebox.showerror("Employee details are required")
    else:
        if Entry!=None:
            messagebox.showerror("Error,This Employee ID is already available in our record")
        else:
            (
            e_idv.get(),
            e_Namev.get(),
            e_Mob_v.get(),
            e_Designationv.get(),
            e_Salaryv.get(),
            e_DOJv.get(),
            e_ID_PROOFv.get(),
            e_Emailv.get(),
            
            messagebox.showinfo("Sucess","Record Added Sucessfully")
            )


