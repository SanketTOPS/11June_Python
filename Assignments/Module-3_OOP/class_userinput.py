class studinfo:
    def printdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)

st=studinfo()
stid=input("Enter an ID:")
stnm=input("Enter a Name:")

st.printdata(stid,stnm)