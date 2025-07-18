import tkinter as tk
from tkinter import *
root = tk.Tk()
l1 = Label(root,text= 'Geeks for geeks')
l1.grid(row=0,column=2)
b1 = Button(root, text='Destroy',width=25,command= root.destroy)
b1.grid(row=1,column=2)
Label(root,text='Your First Name:').grid(row=0)
Label(root,text='Your Second Name:').grid(row=1)
e1 = Entry(root).grid(row=0,column=1)
e2 = Entry(root).grid(row=1,column=1)

root.mainloop()