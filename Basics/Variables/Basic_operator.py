num1=int(input("enter first number= "))   #convert str into int because" " is str
num2=int(input("enter second number= "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
if num2 != 0:
   quotient=num1/num2
else :
    quotient="undefined"  
print("sum= ",sum)
print("diff= ",difference)
print("multiply= ",product)
print("divide= ",quotient)
