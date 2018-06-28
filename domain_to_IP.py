import tkinter  as tk
import socket
from functools import partial

def call_convert(rlabel,inputn):
    ip=socket.gethostbyname(inputn.get())
    rlabel.config(text=ip)

root=tk.Tk()
root.title("Domain To IP Converter")
root.resizable(width=False,height=False)

domainInput=tk.StringVar()

input_label=tk.Label(root,text="Enter the domain",foreground="#ffffff",background="#009688" )
input_label.grid(row=1)
input_entry=tk.Entry(root,textvariable=domainInput)
input_entry.grid(row=1,column=1)

result_label=tk.Label(root)
result_label.grid(row=3,columnspan=4)

call_convert =partial(call_convert,result_label,domainInput)
result_button=tk.Button(root,text="Convert",command=call_convert,background="#ffffff")
result_button.grid(row=2,columnspan=4)

root.mainloop()
root.destroy()
