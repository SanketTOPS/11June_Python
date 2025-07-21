import random
import datetime

fl=open("stdata.txt","a")

n=int(input("Enter a number of students:"))

def getdata():
    #stid=input("Enter an ID:")
    Inserted_at=datetime.datetime.now()
    stid=random.randint(1111,9999)
    stnm=input("Enter a Name:")
    stct=input("Enter a City:")

    fl.write(f"\nInserted_at:{Inserted_at}\nID:{stid}\nName:{stnm}\nCity:{stct}")
    fl.write("\n----------------------\n")


for i in range(n):
    getdata()
    

"""x=datetime.datetime.now().date()
print(x)"""
