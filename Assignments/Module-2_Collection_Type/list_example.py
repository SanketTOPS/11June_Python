data=['python','php','java','html','c++','php','php']
#print(data)

"""print(data[0])
print(data[-1])
print(data[0:3]) #range
print(data[2:])
print(data[:3])
print(len(data))"""

"""if 'PHP' in data:
    print("Yes....")
else:
    print("Noo")"""


# ---------------------------------- #
#print(data)

"""for i in data:
    print(i)"""

#print(data.index('java'))

"""for i in data:
    print(f"{data.index(i)} - {i}")"""

print(data)
#data[2]='android' #update the value
#data.append("react")
#data.insert(2,'css')
#data.remove('java')
#data.pop()
#data.pop(1)
#data.clear()
#del data[3]
#del data
#data.sort()
#data.reverse()
#print(data.count('php'))
#newdata=data.copy()
#print(newdata)


newdata=['html','css','js']
print(newdata)

#print(data+newdata)
data.extend(newdata)
print(data)