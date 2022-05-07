from tkinter import *
def main_screen():
    global screen
    global name_label
    global name
    global date
    global amount
    global name_entry,date_entry,amount_entry
    screen=Tk()
    screen.title("Bank Entries")
    screen.geometry("600x300")
    Label(screen,text="Welcome to Bank Entries Portal",font=("Georgia",20,'bold italic'),fg='blue').pack()
    Label(screen, text="").pack()
    name_label=Label(screen,text="Enter Name : ").pack()
    name=StringVar()
    name_entry=Entry(screen,width=25,textvariable=name).pack()
    date_label=Label(screen,text="Enter Date of Entry : ").pack()
    date=StringVar()
    date_entry=Entry(screen,width=25,textvariable=date).pack()
    amount_label=Label(screen,text="Enter Amount in numbers : ").pack()
    amount=StringVar()
    amount_entry=Entry(screen,width=25,textvariable=amount).pack()
    Label(screen,text="").pack()
    Button(screen,text="Submit",fg='blue',activeforeground='red',command=printdetails).pack()
    Button(screen,text="Reset",fg='blue',activeforeground='red',command=reset_screen).pack()
    screen.mainloop()
def printdetails():
    global getname
    global getdate
    getname=name.get()
    getdate=date.get()
    getamount=amount.get()
    f=open("Bank Entries","a")
    f.write(getname+"-"+getdate+"-"+getamount)
    f.write("\n")
    f.close()
    Label(screen,text="Details Recorded Succesfully !",fg="green").pack()
    print("\r")
    print(getname,"-",getdate,"-",getamount)
def reset_screen():
    screen.destroy()
    main_screen()
main_screen()