import re
text="abbb"
pattern=r"(ab+)"
match=re.fullmatch(pattern,text)
if match:
    print(match.group(1))