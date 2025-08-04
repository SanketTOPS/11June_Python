import re

mystr="This is Python!"

x=re.findall('is',mystr)
print(x)

if x: #TRUE
    print("Match Done!")
else:
    print("Error!")