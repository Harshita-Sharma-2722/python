import re
text="harshita12_"
pattern=r"(\w+)"
match=re.search(pattern,text)
if match:
    print(match.group(1))
else:
    print("not found")