from tkinter import *
from tkinter import messagebox as b
a=Tk()
a.title('ATTENDANCE CALCULATOR')
def process():
    classes = int(Entry.get(e1))
    attended = int(Entry.get(e2))
    attendance=(attended/float(classes))*100
    if attendance >75:
        t=Text(a,height=4,width=30,font=('Times New Roman',16))
        t.insert(INSERT,'You Are Allowed to sit In Exam')
        t.place(x=100,y=300)
    else:
        t=Text(a,height=4,width=30,font=('Times New Roman',16))
        t.insert(INSERT,'Not Allowed For the Exam')
        t.place(x=100,y=300)
Label(a,text='PERCENTAGE',font=('Times New Roman',16)).pack()
Label(a,text='Classes',font=('Times New Roman',16)).place(x=20,y=50)
Label(a,text='Attended',font=('Times New Roman',16)).place(x=20,y=90)
e1=Entry(a,font=('Times New Roman',16),width=15)
e1.place(x=100,y=52)
e2=Entry(a,font=('Time New Roman',16),width=15)
e2.place(x=100,y=92)
img=PhotoImage(file='submit.png')
btn=Button(a,text='Sumbit',image=img,font=('Times New Roman',16),command=process)
btn.place(x=50,y=150)
a.mainloop()