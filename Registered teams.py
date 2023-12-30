from tkinter import *
from tkinter import ttk
import mysql.connector
def king():
    import regclass
def show():
    info = Toplevel()
    info.geometry("925x500")
    info.title("REGISTERED TEAMS")
    info.configure(bg="black")
    photo = PhotoImage(file='C:\\Users\\joe\\Desktop\\fplayer2.png')
    Label(info, image=photo, bg="black").place(x=100, y=2)
    Label(info, text="REGISTERED TEAMS:", bg="black", fg="white", font=('Microsoft YaHei UI Light', 30, 'bold'), width=24,
          height=1, bd=2).place(x=50, y=30)
    b4 = Button(info, text="Add Your Team Now!", bg="white", fg="#1874CD", font=('Microsoft YaHei UI Light', 18, 'bold'),
                width=24, height=1, bd=2, command=king).place(x=825, y=800)

    db = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="football")
    js = db.cursor()
    js.execute("SELECT * FROM PLAYER")
    j=ttk.Treeview(info)
    j.pack(padx=10,pady=200)
    j['show']='headings'
    j['columns']=("player1","player2","player3","player4","player5","teamname")
    j.column("player1",width=200,minwidth=200,anchor=CENTER)
    j.column("player2", width=200, minwidth=200,anchor=CENTER)
    j.column("player3", width=200, minwidth=200,anchor=CENTER)
    j.column("player4", width=200, minwidth=200,anchor=CENTER)
    j.column("player5", width=200, minwidth=200,anchor=CENTER)
    j.column("teamname", width=200, minwidth=200,anchor=CENTER)

    j.heading("player1",text="PLAYER ONE",anchor=CENTER)
    j.heading("player2", text="PLAYER TWO",anchor=CENTER)
    j.heading("player3", text="PLAYER THREE",anchor=CENTER)
    j.heading("player4", text="PLAYER FOUR",anchor=CENTER)
    j.heading("player5", text="PLAYER FIVE",anchor=CENTER)
    j.heading("teamname", text="TEAM NAME",anchor=CENTER)

    h=0
    for k in js:
        j.insert('',h,text="",values=(k[0],k[1],k[2],k[3],k[4],k[5]))
        h+1
    j.pack()
    info.mainloop()
show()
