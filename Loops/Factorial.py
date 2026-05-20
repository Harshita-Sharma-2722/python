num = int(input("enter a number= "))
fact=1
if num<=0:
    print("not exist")
else :
    for no in range(1,num+1):
        fact=fact*no
print("factorial of ", num, "is= ",fact)        
    