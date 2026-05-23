def swap(a,b):
    return b,a
a=int(input("enter 1 no= "))
b=int(input("enter 2 no= "))
a,b=swap(a,b) # swap is a function
print("after swapping=")
print("a= ",a,"b= ",b)