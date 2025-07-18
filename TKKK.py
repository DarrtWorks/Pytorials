import tkinter as tk
from tkinter import *
root = tk.Tk()
l1 = Label(root,text= 'Geeks for geeks')
l1.pack(anchor= CENTER)
b1 = Button(root, text='Destroy',width=25,command= root.destroy)
b1.pack()


root.mainloop()