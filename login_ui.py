from tkinter import *
from tkinter import messagebox
from login_oop import Database1
win=Tk()
win.geometry('450x450')
win.title('Login Form')
win.config(bg='pink')
db=Database1('d:/login.db')
#Functions
def sign_up():
    if ent_email.get()=='' or ent_password.get()=='':
        messagebox.showerror('Empty field','necessary fields must be filled')
        return
    db.insert(ent_firstname.get(),ent_lastname.get(),ent_email.get(),ent_password.get())
    ent_firstname.delete(0,END)
    ent_lastname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_firstname.focus_set()
def sign_in():
    record=db.search(ent_email.get(),ent_password.get())
    print(record)
    if ent_email.get()==record[2] and int(ent_password.get())==record[3]:
        win2=Tk()
        win2.config(bg='pink')
        win2.geometry('400x400')
        win.title('Welcome')
        lbl_welcome=Label(text=f'Welcome {record[0]} {record[1]}',bg='pink',fg='grey')
        lbl_welcome.place(x=180,y=180)
    else:
        messagebox.showerror('failed to log in','No such email previously logged in')
        

#Labels
lbl_firstname=Label(text='Firstname:',bg='pink',font='arial 10 bold')
lbl_firstname.place(x=50,y=20)
lbl_lastname=Label(text='Lastname:',bg='pink',font='arial 10 bold')
lbl_lastname.place(x=50,y=70)
lbl_email=Label(text='Email:',bg='pink',font='arial 10 bold')
lbl_email.place(x=50,y=120)
lbl_necessary1=Label(text='*',bg='pink',font='arial 10 bold',fg='red')
lbl_necessary1.place(x=40,y=120)
lbl_password=Label(text='Password:',bg='pink',font='arial 10 bold')
lbl_password.place(x=50,y=170)
lbl_necessary2=Label(text='*',bg='pink',font='arial 10 bold',fg='red')
lbl_necessary2.place(x=40,y=170)
#Entries
ent_firstname=Entry(width=30)
ent_firstname.place(x=135,y=23)
ent_lastname=Entry(width=30)
ent_lastname.place(x=135,y=73)
ent_email=Entry(width=35)
ent_email.place(x=105,y=123)
ent_password=Entry(width=30)
ent_password.place(x=130,y=173)
#Buttons
btn_signup=Button(text='Sign up ',width=15,bg='white',activebackground='white',fg='blue',activeforeground='blue',command=sign_up)
btn_signup.place(x=100,y=370)
btn_signin=Button(text='Sign in ',width=15,bg='white',activebackground='white',fg='blue',activeforeground='blue',command=sign_in)
btn_signin.place(x=220,y=370)





win.mainloop()