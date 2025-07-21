def getdata():
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stct=input("Enter a City")

    print("---------------")
    print("ID:",stid)
    print("Name:",stnm)
    print("City:",stct)
    print("---------------")

n=int(input("Enter a number of students:"))
for i in range(n):
    getdata()