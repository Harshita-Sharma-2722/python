str1=input("enter first string= ")
str2=input("enter second string= ")
if(str1==str2):
    print("equal")
else:
    print("not equal")
    if len(str1)>len(str2):
        print("first string is longer")
    elif len(str1)<len(str2):
        print("second string is longer")
    else:
        print("both are equal")