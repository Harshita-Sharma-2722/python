def find_max(a,b,c):
    return(max(a,b,c))
print(find_max(4,2,6))    

       # OR
       
def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c :
        return b
    else :
        return c
print(find_max(4,2,6))          