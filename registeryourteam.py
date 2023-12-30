from tkinter import *
from tkinter import messagebox
import mysql.connector



def add():

    teamname =e6.get()
    player1 = e1.get()
    player2 = e2.get()
    player3 = e3.get()
    player4 = e4.get()
    player5 = e5.get()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="football")
    mycursor = mysqldb.cursor()
    try:
        sql = "INSERT INTO  player (player1,player2,player3,player4,player5,teamname) VALUES (%s,%s, %s, %s, %s,%s)"
        val = (player1, player2, player3, player4, player5,teamname)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Team added successfully...")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
def clearitems():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

global e1
global e2
global e3
global e4
global e5
global e6


reg = Toplevel()
reg.geometry("925x500")
reg.title("REGISTER IN FOOTBALL TOURNAMENT")
reg.configure(bg="white")
photo=PhotoImage(file='C:\\Users\\joe\\Desktop\\football-player-34836.PNG')
Label(reg,image = photo,bg="white").place(x=100,y=2)
jk=PhotoImage(file='C:\\Users\\joe\\Desktop\\black adidas3.png')
Label(reg,image = jk,bg="white").place(x=1350,y=850)
Label(reg, text="Player1:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'),width=12, height=1, bd=2).place(x=50, y=50)
e1=Entry(reg, width=25, bd=2)
e1.place(x=250, y=52)
Label(reg, text="Player 2:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'),width=12, height=1, bd=2).place(x=50, y=90)
e2 = Entry(reg, width=25, bd=2)
e2.place(x=250, y=92)
Label(reg, text="Player 3:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'),width=12, height=1, bd=2).place(x=50, y=130)
e3 = Entry(reg, width=25, bd=2)
e3.place(x=250, y=132)
Label(reg, text="Player 4:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'),width=12, height=1, bd=2).place(x=50, y=170)
e4 = Entry(reg, width=25, bd=2)
e4.place(x=250, y=172)
Label(reg, text="Player 5:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'),width=12, height=1, bd=2).place(x=50, y=210)
e5 = Entry(reg, width=25, bd=2)
e5.place(x=250, y=212)
Label(reg, text="Team name:", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 16, 'bold'), width=12, height=1, bd=2).place(x=50, y=250)
e6 = Entry(reg, width=25, bd=2)
e6.place(x=250, y=252)
Label(reg, text="Amount to be paid: 5200 Rs", bg="white", fg="#1874CD",font=('Microsoft YaHei UI Light', 16, 'bold'), width=24, height=1, bd=1).place(x=50, y=300)
Label(reg, text="Last Date of registration:26/08/2022", bg="white", fg="#1874CD",font=('Microsoft YaHei UI Light', 16, 'bold'), width=32, height=1, bd=1).place(x=10, y=340)
b3 = Button(reg, text="Add", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 18, 'bold'), width=12, height=1, bd=2, command=add).place(x=625, y=325)
b4 = Button(reg, text="Clear items", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 18, 'bold'), width=12, height=1, bd=2, command=clearitems).place(x=625, y=400)
