numbers = {1, 2, 3, 2, 4, 3, 5, 1, 6}
print(numbers)
lst= input("enter list name= ").split()
x=list(set(lst))
print("before convert",lst)
print("after convert",x)

#or

numbers = {1, 2, 3, 2, 4, 3, 5, 1, 6}
print(numbers)

lst = input("Enter values: ")

print("Before convert:", lst)

x = list(set(lst))

print("After convert:", x)