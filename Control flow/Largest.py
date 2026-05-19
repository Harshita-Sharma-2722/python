a=int(input("enter first no= "))
b=int(input("enter second no= "))
c=int(input("enter third no= "))
if(a>=b and a>=c):
    print("a is largest")
elif(b>=c and b>=a):
    print("b is largest")
else:
    print("c is largest")