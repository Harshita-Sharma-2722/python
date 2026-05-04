temp=float(input("enter temp in celsius= "))
if(temp<0):
   print("freezing")
elif(temp>=0 and temp<=15):
    print("cold")
elif(temp>=16 and temp<=30):
    print("warm")
else:
    print("hot")