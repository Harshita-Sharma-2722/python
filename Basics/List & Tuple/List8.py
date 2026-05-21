#check all elements are unique

list=[1,2,3,4,5]
if len(list)==len(set(list)):
    print("all elements are unique")
else:
    print("all elements are not unique")