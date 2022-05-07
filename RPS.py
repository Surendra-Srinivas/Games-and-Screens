from tkinter import *
import random
USER_SCORE=0
COMP_SCORE=0
print("\r")
def random_comp_choice():
    return random.choice(['Rock','Paper','Scissors'])
def Mybutton(root):
    f=Frame(root,height=500,width=700)
    f.propagate(0)
    f.pack()
    b1=Button(f,text="Rock",fg='Blue',activeforeground="red",font=("Georgia",26),command=rock)
    b2=Button(f,text="Paper",fg='Blue',activeforeground="red",font=("Georgia",26),command=paper)
    b3=Button(f,text="Scissors",fg='Blue',activeforeground="red",font=("Georgia",26),command=scissors)
    b1.place(x=150,y=100)
    b2.place(x=150,y=140)
    b3.place(x=150,y=180)
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    if human_choice==comp_choice:
        print("Tie")
    if human_choice == 'Rock' and comp_choice == 'Paper':
        print("Computer Win !")
        COMP_SCORE+=1
    if human_choice == 'Rock' and comp_choice == 'Scissors':
        print("Player Win !")
        USER_SCORE+=1
    if human_choice == 'Paper' and comp_choice == 'Rock':
        print("Player Win !")
        USER_SCORE+=1
    if human_choice == 'Paper' and comp_choice == 'Scissors':
        print("Computer Win !")
        COMP_SCORE+=1
    if human_choice == 'Scissors' and comp_choice == 'Rock':
        print("Computer Win !")
        COMP_SCORE+=1
    if human_choice == 'Scissors' and comp_choice == 'Paper':
        print("Player Win !")
        USER_SCORE+=1
    text_area =Text(root,height=6,width=20,bg="black",font=("Calibiri",20,'italic'),fg='White')
    text_area.place(x=150,y=250)
    answer = "Your Choice: {uc}\nComputer's Choice : {cc}\nYour Score : {u}\nComputer Score : {c} ".format(uc=human_choice,cc=comp_choice,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(END,answer)
def rock():
    global USER_SCORE
    global COMP_SCORE
    user_choice="Rock"
    comp_choice=random_comp_choice()
    result(user_choice,comp_choice)
def paper():
    global USER_SCORE
    global COMP_SCORE
    user_choice="Paper"
    comp_choice=random_comp_choice()
    result(user_choice,comp_choice)
def scissors():
    global USER_SCORE
    global COMP_SCORE
    user_choice="Scissors"
    comp_choice=random_comp_choice()
    result(user_choice,comp_choice)
root=Tk()
root.title("Rock Paper Scissors")
Mybutton(root)
root.mainloop()




