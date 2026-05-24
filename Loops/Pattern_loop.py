#upper half
for i in range(1,6):
    for j in range (i):
        print("*",end=" ")
    print()
#lower half    
for i  in range(4,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()    
    
    
             #or
             
a = int(input("Enter the no of time you want star to get print: "))
for i in range (1,a+1):
    print("*" * i)
for i in range (a-1 , 0 , -1):
    print("*" *i)                 