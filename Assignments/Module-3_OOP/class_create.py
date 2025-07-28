class studinfo:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is studinfo class.")
    
    def sum(self,a,b):
        print("Sum:",a+b)


st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.sum(34,66)

