#leap year= divided by 4 and 400 but nit divisible by 100

year=int(input("enter a year= "))
if(year%4==0 and year%100!=0) or(year%400==0):
    print("leap year")
else:
    print("not a leap year")