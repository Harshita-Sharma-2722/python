import re
text="Hello Hyy"
pattern=r"([A-Z][a-z]+)"
match=re.findall(pattern,text)
if match:
    print(match)