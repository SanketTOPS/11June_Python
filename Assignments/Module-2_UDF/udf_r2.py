def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

n=int(input("Enter number of students!"))

for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stsub=input("Enter a Subject:")
    getdata(stid,stnm,stsub)