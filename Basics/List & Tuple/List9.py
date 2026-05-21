# replace last item with new value if found

list=[1,2,3,4]
old_value=4
new_value=6
if list[-1]==old_value:
    list[-1]=new_value
print(list)    