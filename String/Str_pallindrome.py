text=input("enter a text= ")
if text==text[::-1]: # this mean [start:stop:step],here step is -1
    print("pallindrome")
else:
    print("not pallindrome")