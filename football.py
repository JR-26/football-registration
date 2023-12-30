from tkinter import *
from tkinter import messagebox
import mysql.connector

def king():
    import regclass
def queen():
    import unregister
def minister():
    import aboutus





match=Tk()
match.geometry("925x500")
match.title("FIFA FOOTBALL TOURNAMENT")
match.configure(bg="black")

photo=PhotoImage(file='C:\\Users\\joe\\Desktop\\fifa2.PNG')
Label(match,image = photo,bg="black").place(x=10,y=2)


b1=Button(match,text="R e g i s t e r",bg="black",fg="white",font=('Microsoft YaHei UI Light',24,'bold'),width=12,height=1,bd=2,command=king).place(x=625,y=150)
b2=Button(match,text="v i e w  r e g i s t e r e d  t e a m s ",bg="black",fg="white",font=('Microsoft YaHei UI Light',14,'bold'),width=30,height=1,bd=2,command=queen).place(x=540,y=250)
b3=Button(match,text="About us",bg="black",fg="#1874CD",font=('Microsoft YaHei UI Light',18,'bold'),width=12,height=1,bd=2,command=minister).place(x=625,y=325)
name=Label(match,text="J u s t P l a y \n\n H a v e  F u n \n\n E n j o y T h e G a m e! ",bg="black",fg="#858585",font=('helvetica',12,'italic')).place(x=150,y=375)


match.mainloop()
