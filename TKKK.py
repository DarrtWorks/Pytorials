import tkinter as tk
from tkinter import *
root = tk.Tk()
l1 = Label(root,text= 'Geeks for geeks')
l1.grid(row=0,column=2)
b1 = Button(root, text='Destroy',width=25,command= root.destroy)
b1.grid(row=1,column=2)
Label(root,text='Your First Name:').grid(row=0,)
Label(root,text='Your Second Name:').grid(row=1)
e1 = Entry(root).grid(row=0,column=1)
e2 = Entry(root).grid(row=1,column=1)
var1 = IntVar()
Checkbutton(root, text='male', variable=var1).grid(row=2,column=0, sticky=W, columnspan=2)
#we can call grid on checkbutton directly
#instead of assigning it to a variable
#as we are not using it later to modify the checkbutton
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).grid(row=2,column=1, columnspan=2)
Lb = Listbox(root)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'C#') 
Lb.grid(columnspan=2)
#Function to get user input from Entry field
#and print it to the console
def GetPlayerInput():
    UserInput = EntryField1.get()
    print(UserInput)
    
    
#Create an Entry field for user input
#and a button to submit the input    
EntryField1 = Entry(root)
EntryField1.grid(row=3, column=3, columnspan=2)
Button(root, text='Submit', command=GetPlayerInput).grid(row=4, column=3, columnspan=2)


#listbox.grid must be called after the insert method
#to ensure the listbox is populated before displaying it


#Can use Radiobutton instead of Checkbutton for single selection
root.mainloop()