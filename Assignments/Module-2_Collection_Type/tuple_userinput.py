data=[] #list obj

n=int(input("Enter number of elements:"))

for i in range(n):
    lang=input("Enter your language:")
    data.append(lang)

print(tuple(data))


