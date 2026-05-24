import re 
text="i am python"
pattern=r"(am)"
match=re.search(pattern,text)
if match:
    print("found")