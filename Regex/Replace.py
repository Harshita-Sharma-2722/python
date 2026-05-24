import re
text="I am going"
pattern=r"(\s)"
match=re.sub(pattern,"_",text)
if match:
    print(match)