def pallindrome(text):
    if len(text)<=1:
        return True
    if text[0]!=text[-1]:
        return False
    return pallindrome(text[1:-1])
word= input("enter a text= ")
if pallindrome(word):
    print("pallindrome")
else:
    print("not pallindrome")