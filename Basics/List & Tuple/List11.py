numbers=[]
while True:
    num=int (input("enter a no= "))
    if num==0:
        break
    numbers.append(num)
numbers.sort()
print(numbers)    