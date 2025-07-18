import numpy as np;

list = np.array([])


while(True):

 inp = int(input("1 for adding an element, 2 for removing an element & 3 for viewing your list "))

 St = ""

 if(inp == 1):
    while(St != "STOP"):
        In = input("Element:")
        St = input("please enter 'STOP' to stop adding elements")
        list = np.append(list,In)
        print("list =",list)

        

 if(inp == 3):
    print(list)

 if(inp == 2):
    print("List =",list)
    El_No = int(input("Element number that you want to remove:"))
    list = np.delete(list,El_No-1)
    print("List =", list)

