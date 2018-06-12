from Tkinter import *
from Tkinter import Tk

root =Tk()
root.geometry("300x200")
root.title("BUTTONS")

button1=Button(text="BUTTON1",relief=FLAT).pack()
button2=Button(text="BUTTON2",relief=SUNKEN).pack()
button3=Button(text="BUTTON3",relief=GROOVE).pack()
button4=Button(text="BUTTON4",relief=RIDGE).pack()
button5=Button(text="BUTTON5",relief=RAISED).pack()



root.mainloop()