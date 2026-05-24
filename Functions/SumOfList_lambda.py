#reduce() is used when we want to combine all elements of a list into a single value.

from functools import reduce
num=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)