from tkinter import *
import os
def main_account_screen():
    global main_screen
    main_screen=Tk()
    main_screen.geometry("600x300")
    main_screen.title("SFDC Portal")
    Label(main_screen,text="Welcome to Surendra's FrameDesigner Consortium",font=("Georgia",20,'bold italic'),fg='blue').pack()
    Label(main_screen, text="").pack()
    Label(main_screen,text="New user ?").pack()
    Button(main_screen,text="Register",height=2,width=25,fg='black',activeforeground='red',command=register).pack()
    Label(main_screen,text="").pack()
    Label(main_screen,text='Already a User?').pack()
    Button(main_screen,text='Login',height=2,width=25,fg='black',activeforeground='red',command=login).pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="").pack()
    Button(main_screen,text='Help!',height=2,width=10,fg='Purple',activeforeground='red',command=help_me).pack()
    main_screen.mainloop()
def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry
    register_screen=Toplevel(main_screen)
    register_screen.title("Registration")
    register_screen.geometry("600x300")
    username=StringVar()
    password=StringVar()
    Label(register_screen,text="Please provide the Details",font=("Georgia",20,'bold')).pack()
    username_label=Label(register_screen,text="Username : ",fg='red',font=("Georgia",14,'bold'))
    username_label.pack()
    username_entry=Entry(register_screen,width=25,textvariable=username,show="*")
    username_entry.pack()
    password_label=Label(register_screen,text="Password : ",fg='red',font=("Georgia",14,'bold'))
    password_label.pack()
    password_entry=Entry(register_screen,width=25,textvariable=password)
    password_entry.pack()
    Label(register_screen,text="----------------------").pack()
    Button(register_screen,text="Register",fg='blue',activeforeground='red',command=register_user).pack()
    Button(register_screen,text="Go Back",fg='blue',activeforeground='red',command=delete_register_screen).pack()
def register_user():
    username_info=username.get()
    password_info=password.get()
    f=open("Details","a")
    f.write(username_info+'\n')
    f.write(password_info+'\n')
    f.write("\n")
    f.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(register_screen,text="Registration Succesful !",fg='green').pack()
def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    login_screen=Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("600x300")
    username_verify=StringVar()
    password_verify=StringVar()
    Label(login_screen,text="Enter the Credentials :",font=("Georgia",20,'bold')).pack()
    Label(login_screen,text="").pack()
    Label(login_screen,text="Username : ",fg='red',font=("Georgia",14,'bold')).pack()
    username_login_entry=Entry(login_screen,width=25,textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen,text="Password : ",fg='red',font=("Georgia",14,'bold')).pack()
    password_login_entry=Entry(login_screen,width=25,textvariable=password_verify,show="*")
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen,text="Login",fg='blue',activeforeground='red',command=login_verify).pack()
    Button(login_screen,text="Go Back",fg='blue',activeforeground='red',command=delete_login_screen).pack()
def login_verify():
    global verify
    global username1
    global password1
    username1=username_verify.get()
    password1=password_verify.get()
    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)
    f=open("Details","r")
    verify=f.read().splitlines()
    if username1 in verify:
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
    f.close()
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    if username1=='Surendra':
        Button(login_success_screen, text="Look inside", command=show_app_screen).pack()
def show_app_screen():
    global app_screen
    app_screen=Toplevel(main_screen)
    app_screen.title("MyMacbook")
    app_screen.geometry("600x200")
    Label(app_screen, text="Access my applications Right from here.",font=("Georgia",20,'bold italic')).pack() 
    Button(app_screen, text="iMessages", command=open_messages).pack()
    Button(app_screen, text="Photos", command=open_photos).pack()
def open_messages():
    import os
    os.system("/System/Applications/Messages.app/Contents/MacOS/Messages")
def open_photos():
    import os
    os.system("/System/Applications/Photos.app/Contents/MacOS/Photos")
def help_me():
    global help_screen
    help_screen=Toplevel(main_screen)
    help_screen.title("Get your help here !")
    help_screen.geometry("500x180")
    Label(help_screen, text="").pack()
    Label(help_screen, text="").pack()
    Label(help_screen,text='Contact : 9505245988',fg='black',font=("Georgia",20,'bold')).pack()
    Label(help_screen,text='email id : surendranaik242@gmail.com',fg='black',font=("Georgia",20,'bold')).pack()
    Label(help_screen, text="").pack()
    Button(help_screen, text="Go Back",fg='blue',activeforeground='red', command=delete_help_screen).pack()
def delete_help_screen():
    help_screen.destroy()
def delete_login_success():
    login_success_screen.destroy()        
def delete_register_screen():
    register_screen.destroy()
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen=Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password! ").pack()
    Button(password_not_recog_screen, text="Go Back", command=delete_password_not_recognised).pack()
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def user_not_found():
    global user_not_found_screen
    user_not_found_screen=Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Invalid Username! ").pack()
    Button(user_not_found_screen, text="Go Back", command=delete_user_not_found_screen).pack()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
def delete_login_screen():
    login_screen.destroy()
main_account_screen()         