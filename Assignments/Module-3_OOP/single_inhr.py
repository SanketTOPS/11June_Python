class studinfo:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter an ID:")
        self.stnm=input("Enter a Name:")

class result(studinfo):
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

rs=result()
rs.getdata()
rs.printdata()