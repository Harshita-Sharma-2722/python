text=input("enter a text= ")
letters=0
digit=0
special_symbol=0
for ch in text: # one character at a time
    if ch.isalpha(): #check letters
        letters=letters+1
    elif ch.isdigit(): #check digits
        digit=digit+1
    else:
        special_symbol=special_symbol+1 #check symbol
print("letters= ",letters)
print("digit= ",digit)
print("symbol= ",special_symbol)                