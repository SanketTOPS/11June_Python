import re

mystr="This is Python!"

x=re.match("This",mystr)
print(x)

if x: #TRUE
    print("Match Done!")
else:
    print("Error!")