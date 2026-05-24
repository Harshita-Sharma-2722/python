import random
import string
def pass_gen(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=""
    for i in range (length):
        password=password+random.choice(characters)
    return password
print("password= ",pass_gen(8))    
    
    