marks=int(input("enter a marks= " ))
if marks>=80:
    print("excellent")
elif marks>=65 and marks<=80:
    print("good")
elif marks>=50 and marks<=65:
    print("pass")
elif marks<=50:
    print("fail")
else:
    print("nothing")