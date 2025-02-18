#========= LIBRAIRIES =========
from  tkinter import *
from tkinter import ttk
#import this fonts :https://fonts.google.com/specimen/Oswald

#========== INFO ==============
login=Tk()
login.title("Login by xspy")
login.geometry("500x500")
login.resizable(0,0)
login.iconbitmap("login-icon-kali-test.ico")
login.config(bg="#efefd0")
#========== TITLE ==============
title =Label(login,text="Login by Xspy",font=("Oswald",15),bg="#f15025",fg="#191919")
title.pack(fill=X)
#========== FRAME ==============
frame1=Frame(login, width="350" , height="350", bg ="whitesmoke")
frame1.pack(pady=30)
#========== IMAGE ==============
photo=PhotoImage(file="login.png" )
ph_place=Label(frame1,image=photo)
ph_place.place(x=150,y=10)
#========== LABEL ==============
lb1=Label(frame1,text="Username :",font=("Courier",15),bg="whitesmoke")
lb1.place(x=20,y=150)
lb2=Label(frame1,text="Password :",font=("Courier",15),bg="whitesmoke")
lb2.place(x=20,y=200)  
#========== ENTRY ==============
en1=Entry(frame1)
en1.place(x=150,y=157)
en2=Entry(frame1)
en2.place(x=150,y=207)
#========== BUTTON ==============
bt1=Button(frame1,text="Login",font=("Courier",15),bg="#02c39a", width=10)
bt1.place(x=20,y=250)
bt2=Button(frame1,text="SIGN IN",font=("Courier",15),bg="#fb4b4e", width=10)
bt2.place(x=190,y=250)

#========= CHECKBUTTON ===========
check1=Checkbutton(frame1,text="Remember me",font=("Courier",10),bg="whitesmoke")
check1.place(x=20,y=300)
copyright=Label(login,text="© 2025 https://github.com/xcyberspy",font=("Courier",10),bg="#efefd0")
copyright.place(x=150,y=420)
#========== MAINLOOP =============
login.mainloop()