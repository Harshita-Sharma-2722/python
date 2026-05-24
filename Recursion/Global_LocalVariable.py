x=30
def demo():
    global x
    x=40
    y=20
    print("inside function=")
    print("x= ",x)
    print("y= ",y)
demo()
print("outside function= ")
print("x= ",x)    