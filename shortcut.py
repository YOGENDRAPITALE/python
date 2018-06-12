import Tkinter as tk
import webbrowser
import datetime
from Tkinter import *
import os
from datetime import date
from datetime import time

today=date.today()
def doorbell (event):
	print("You rang a door bell!")

def open_cp(event):
	webbrowser.open_new_tab("https://www.youtube.com")
	
def date(event):
	print(today)

def time(event):
		print(todaytime)
def open_cp1(event):
		webbrowser.open_new_tab("https://www.facebook.com")
		
def open_cp2(event):
		webbrowser.open_new_tab("https://www.google.co.in")
window=tk.Tk()

window.title('App')
window.geometry("720x360")
window.configure(background='red')
#mi=PhotoImage(file="C:\Users\Yogi\Pictures\\pic.jpeg")

alabel=tk.Label(text="Alert",font=("arial",14,"bold"),bd=10,width=10,relief="sunken")
alabel.grid(column=0,row=0)

blabel=tk.Label(text="Youtube",font=("arial",14,"bold"),bd=10,width=10,relief="sunken")
blabel.grid(column=1,row=0)

clabel=tk.Label(text="Date",font=("arial",14,"bold"),bd=10,width=10,relief="sunken")
clabel.grid(column=2,row=0)

dlabel=tk.Label(text="Facebook",font=("arial",14,"bold"),bd=10,width=10,relief="sunken")
dlabel.grid(column=3,row=0)

elabel=tk.Label(text="GOOGLE",font=("arial",14,"bold"),bd=10,width=10,relief="sunken")
elabel.grid(column=4,row=0)

button = tk.Button(window,text="DoorBell",relief=RAISED,width=10)
button.grid(column=0)

button2 = tk.Button(window,text="YouTube",relief=RAISED,width=10)
button2.grid(column=1,row=1)

button3 = tk.Button(window,text="Date",relief=RAISED,width=10)
button3.grid(column=2,row=1)
#button3.configure(image=mi,compound=RIGHT)
button4=tk.Button(window,text="Facebook",relief=RAISED,width=10)
button4.grid(column=3,row=1)

button5=tk.Button(window,text="Google",relief=RAISED,width=10)
button5.grid(column=4,row=1)

button.bind("<Button-1>",doorbell)
button2.bind("<Button-1>",open_cp)
button3.bind("<Button-1>",date)
button4.bind("<Button-1>",open_cp1)
button5.bind("<Button-1>",open_cp2)

window.mainloop()