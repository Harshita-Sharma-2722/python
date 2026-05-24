import re
text="2563421523"
pattern=r"(\d{10})"
match=re.fullmatch(pattern,text)
if match:
 print(match.group(1))