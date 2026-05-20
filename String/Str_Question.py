reg_no=input("enter a reg no= ")
sum_digit=0
count=0
for ch in reg_no:
    if ch.isdigit():
        sum_digit=sum_digit+int(ch)
        count=count+1
average = sum_digit / count

print("Sum =", sum_digit)
print("Average =", average)        