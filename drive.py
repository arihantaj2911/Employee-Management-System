
from tkinter import *
import sqlite3
from tkinter import messagebox
import re







def clear():
        #clear output area
        #   output.delete(0.0,END)

        entry_name.delete(0,END)
        entry_password.delete(0,END)
        entry_contact.delete(0,END)
        entry_email.delete(0,END)
        entry_age.delete(0,END)
        #clear checkbox and radio
        checkbox1.set(0)
        checkbox2.set(0)
        checkbox3.set(0)
        gender.set(0)
    


#Callback functions

def checkname(name):
    if name.isalnum():
        return True
    if name == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ name[-1])
        return False

"""
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\])    Require that at least one special character appear anywhere in the string
.{8,32}                                      The password must be at least 8 characters long, but no more than 32
$                                            Match the end of the string.
"""
   
def checkpassword(password):
        if len(password)<=20:
                if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                        return True
                        
                    
                messagebox.showwarning("Invalid","Enter valid password")
                return False
        else:
                messagebox.showwarning("Invalid","Length try to exceed")
                return False

def checkcontact(con):
        if con.isdigit():
            return True
        if len(str(con))== 0:
            return True
        
        
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
        
        
def checkemail(email):
        if len(email)>7:
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                    return True
                    
                
                else:
                    messagebox.showwarning("Alert","Invalid E-mail enter by user")
                    return False
        else:
            messagebox.showwarning("Alert","Email length is too small")


 #validate all field at submit time
def validations():
    x =y = 0
    if name.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif password.get() =="" :
        messagebox.showinfo("Alert","Enter Password")
    elif contact.get() == "" or len(contact.get())!=10:
        messagebox.showinfo("Alert","Enter valid Contact ")
    elif email.get() =="":
        messagebox.showinfo("Alert","Enter Email")
    elif age.get() == "": 
        messagebox.showinfo("Alert","Enter Age")
    elif gender.get() ==0:
        messagebox.showinfo("Alert","Select Gender")
    elif country.get() == "" or country.get() == "Select your country":
        messagebox.showinfo("Alert","Select country")
    elif checkbox1.get()==0 and checkbox2.get()==0 and checkbox3.get()==0:
        messagebox.showinfo("Alert","Select language")
    elif email.get()!=None and password.get()!= None:
        
        x = checkemail(email.get())
        y = checkpassword(password.get())
        print(x,y)
    if (x == True) and (y == True):
               prog = []
               name1=name.get()
               pas1=password.get()
               cont1=contact.get()
               email1=email.get()
               age1=age.get()
               gvar=gender.get()
               cnt = country.get()
               prog = checkbox1.get(),checkbox2.get(),checkbox3.get()
               prog = str(prog)
               #print(name1,pas1,cont1,email1,age1,gvar,cnt,prog,type(name1),type(pas1),type(cont1),type(email1),type(age1),type(gvar),type(cnt),type(prog))
               #connection with db   
               conn = sqlite3.connect('Register1.db')
               with conn:
                   cursor=conn.cursor()
                   #querries
                   cursor.execute('CREATE TABLE IF NOT EXISTS  Registration(Name TEXT,Password TEXT,Contact Text,Email TEXT,Age Text,\
                                  Gender Number,Country Text,Prog Text)')
                   cursor.execute('INSERT INTO Registration(Name,Password,Contact,Email,Age,Gender,Country,Prog) VALUES(?,?,?,?,?,?,?,?)',
                                  (name1,pas1,cont1,email1,age1,gvar,cnt,prog))

               conn.commit()
               
def view():
        lx = [name.get(),"\n",password.get(),"\n",contact.get(),"\n",email.get(),"\n",
              age.get(),"\n",gender.get(),"\n",country.get(),"\n",checkbox1.get(),"\n",checkbox2.get(),"\n",checkbox3.get()]
        messagebox.showinfo("Details",lx
                            )
        

        
      

    



            
            
            
        

        
    
        
        
        
        
        
    
        
            
            
        
                        
                                
#GUI
   
win = Tk()
win.geometry("500x600")
win.title("Registration Form")                        
win["bg"] = "sky blue"                     
        
        
#creating data selection variable on gui
name  = StringVar()
password = StringVar()
contact =StringVar()
email = StringVar()
age = StringVar()
gender = IntVar()
country = StringVar()
checkbox1 = IntVar()

checkbox2 = IntVar()
checkbox3 = IntVar()

#Form Title
label_title = Label(win,text ="Registration Form",width = 20,font = ("bold",20)).place(x=70,y=53)


#Create fields
label_name = Label(win,text = "Your Name",width = 20).place(x = 70,y = 130)
entry_name = Entry(win,width = 20,textvariable = name)
entry_name.place(x = 240,y = 130)
validate_name = win.register(checkname)  #validation register
entry_name.config(validate = "key",validatecommand = (validate_name,"%P")) #validation configure

label_password = Label(win,text = "Password",width = 20).place(x = 70,y = 180)
entry_password = Entry(win,textvariable =password,width = 20)
entry_password.place(x = 240,y = 180)


label_contact = Label(win,text ="Contact",width = 20).place(x = 70,y = 230)
entry_contact = Entry(win,textvariable = contact,width = 20)
entry_contact.place(x = 240,y = 230)
validate_contact= win.register(checkcontact)  #validation register
entry_contact.config(validate = "key",validatecommand = (validate_contact,"%P"))

label_email = Label(win,text ="Email Id",width = 20).place(x = 70,y = 280)
entry_email = Entry(win,textvariable = email,width = 20)
entry_email.place(x = 240,y = 280)

label_age = Label(win,text = "Your Age",width = 20).place(x = 70,y = 330)
entry_age = Spinbox(win,textvariable = age,from_ = 1,to_ = 150 )
entry_age.place(x = 240,y = 330)

label_gender = Label(win,text = "Gender",width = 20).place(x = 70,y = 380)
g_radio_male = Radiobutton(win, text="Male",padx = 5, variable=gender ,value= 1).place(x=240,y=380)
g_radio_female =  Radiobutton(win, text="Female",padx = 20, variable=gender, value= 2).place(x=300,y=380)


label_country = Label(win,text = "Your Country",width = 20).place(x = 70,y = 420)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
droplist=OptionMenu(win,country, *list1)
droplist.config(width=15)
country.set('Select your country') 
droplist.place(x=240,y=420)

label_prog = Label(win,text = "Programming",width = 20).place(x = 70,y = 460)
entry_check1 = Checkbutton(win, text="java", variable= checkbox1).place(x=240,y=460)
entry_check2 = Checkbutton(win, text="Python", variable= checkbox2).place(x=290,y=460)
entry_check3 = Checkbutton(win, text="C", variable= checkbox3).place(x=360,y=460)

Button(win, text='Submit',width=10,bg='blue',fg='white',command  = validations).place(x=180,y=500)
Button(win, text='Clear Data',width=10,bg='blue',fg='white',command = clear).place(x=50,y=500)
Button(win, text='Check',width=10,bg='blue',fg='white',command = view).place(x=320,y=500)

win.mainloop()     
            
            
            
        
        

        
        
        
        

        
        
        
        
        

        