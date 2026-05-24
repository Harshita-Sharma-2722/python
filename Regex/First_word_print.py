import re
text="hello world"
pattern=r"(\w+)"
match=re.search(pattern,text)
if match:
    print(match.group(1))