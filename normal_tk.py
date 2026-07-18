import tkinter as tk#module for creating frontend
from tkinter import messagebox
r=tk.Tk()# initialize function
r.title("chatbot")#title
r.geometry("1500x900")#1500 width,900 height
l=tk.Label(r,text="name")#it visulize name content in frame page
l.place(x=150,y=200)
e=tk.Entry(r)
e.place(x=250,y=200)
def msg():# action performance
    messagebox.showinfo("msg","hello")
    
b=tk.Button(r,text="click",command=msg)#if i click this but it will perform
b.place(x=150,y=250)
r.mainloop()#forntend visualization