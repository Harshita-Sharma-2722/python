import re
text="I am going"
pattern=r"(\s)"
match=re.sub(pattern,"",text)
if match:
    print(match)