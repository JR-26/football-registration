from tkinter import *
about=Toplevel()
about.geometry("925x500")
about.title("ABOUT FIFA")
about.configure(bg="white")

Label(about, text="ABOUT US:", bg="white", fg="#FFB6C1", font=('Microsoft YaHei UI Light', 30, 'bold'),width=12, height=1, bd=2).place(x=50, y=30)
Label(about, text="FIFA football tournament is a national 5 v 5 football tournament coducted for the men of age between 15 to 20 .\n It is a knockout tournament each team  should  win every match inorder to qualify to the next round."
      , bg="white", fg="#F4A460", font=('Microsoft YaHei UI Light', 16, 'italic'),width=100, height=5, bd=2).place(x=10, y=80)
Label(about, text="WINNER:", bg="white", fg="#40E0D0", font=('Microsoft YaHei UI Light', 30, 'bold'),width=20, height=1, bd=2).place(x=50, y=200)


Label(about, text="The winning team will be awarded with 5 lakh ruppees and a trophy\n The runners will be awarded with 2.5 lakhs and a trophy\n Others will get a participation certificate."
      , bg="white", fg="#87CEFA", font=('Microsoft YaHei UI Light', 16, 'italic'),width=100, height=5, bd=2).place(x=0, y=250)
Label(about, text="PAYMENT:", bg="white", fg="#40E0D0", font=('Microsoft YaHei UI Light', 30, 'bold'),width=20, height=1, bd=2).place(x=50, y=400)
Label(about, text="THe Registration fee can be paid in our office once you register your team\n(Note:Registration fee can be paid only by offline,We don't encourage online payments!."
      , bg="white", fg="#87CEFA", font=('Microsoft YaHei UI Light', 16, 'italic'),width=100, height=5, bd=2).place(x=0, y=450)
Label(about, text="HAPPY FOOTBALLING!:", bg="white", fg="#33A1C9", font=('Microsoft YaHei UI Light', 30, 'bold'),width=20, height=1, bd=2).place(x=500, y=700)
