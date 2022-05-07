"""colour1=random.choice(colours)
colour2=random.choice(colours)
class colourgame:
    
    def startgame(self,event):
        if time==30:
            self.countdown()
        nextcolour()
    
    def __init__(self,root):
        self.f=Frame(root,height=400,width=400)
        self.f.propagate(0)
        self.f.pack()
        self.inst=Label(self.f,text="Type the colour of the text, not the TEXT.",fg='black',font=("Georgia",18,'bold'))
        self.inst.pack()
        self.e=Entry(fg='black',font=("Arial",18))
        self.e.place(x=100,y=250)
        self.e.bind("<Return>",self.nextcolour)
        self.timeLabel =Label(root, text = "Time left: " +str(time), font = ('Helvetica', 20))
        self.timeLabel.place(x=140,y=80)
        self.scorelabel=Label(self.f,text="Press Enter to start:",font = ('Helvetica', 20),fg='Black')
        self.scorelabel.place(x=120,y=200)
        self.label=Label(self.f,text=colour1,font=("Georgia",60,'bold'),fg=colour2)
        self.label.place(x=140,y=120)
    def countdown(self):
        global time
        if time > 0:
            time-=1
        self.timeLabel.config(text = "Time left: "+ str(time))
        self.timeLabel.after(1000, countdown)
    def nextcolour(self,event):
        global score,time
        if time>0:
            if self.e.get()==colour2:
                print("player win!")
                score+=1
            else:
                print("Loose")
            self.label.config(fg=colour2,text=colour1)
            self.e.delete(0,END)
            self.scorelabel.config(text = "Score: " + str(score))
          
            
    
root=Tk()
cg=colourgame(root)
root.title("Colour Game.")
root.mainloop()
"""
import random
from tkinter import *
from tkinter import messagebox
colours=['red','blue','green','pink','black','yellow','orange','white','purple','brown']
time=36
score=0
def startgame(event):
    l2.config(text="")
    if time==36:
        countdown()
    nextcolour()
def nextcolour():
    global score,time
    if time>0:
        e1.focus_set()
        if e1.get().lower()==colours[1].lower(): # What is lower()?
            score+=1
        e1.delete(0,END)
        random.shuffle(colours)
        text.config(fg=str(colours[1]),text=str(colours[0]),bg=colours[6])
        scorelabel=Label(text="Score is : "+str(score),fg='black')
        scorelabel.place(x=200,y=230)
    if time==0:
        messagebox.showinfo("GAME OVER",f"GAME OVER , Hey your time is up , and your score is : "+str(score))
def countdown():
    global time
    if time>0:
        time-=1
        t=Label(text='Time Left : '+str(time),fg='red' )
        t.place(x=200,y=200)
        t.after(1000,countdown)
root=Tk()
root.geometry("500x500")
root.title("Coolour Game!")
l1=Label(root,text="Type the colour of the text,not the Text!",font=("Gerogia",16,'bold'))
l1.pack()
l2=Label(root,text="Press Enter to start the Game ",font=("Gerogia",14))
l2.pack()
e1=Entry(root,width=15,fg='black')
e1.place(x=160,y=260)
e1.focus_set() # Goto Definition to know more. 
text=Label(root,font=("Georgia",100))
text.pack()
root.bind("<Return>",startgame)
root.mainloop()
"""
2021-04-06 17:54:03.952 Python[38250:719116] Warning: Expected min height of view: (<NSButton: 0x7ffb85b19310>) to be less than or equal to 30 but got a height of 32.000000. This error will be logged once per view in violation.

"""



