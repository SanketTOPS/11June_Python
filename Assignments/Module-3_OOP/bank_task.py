import random
class ac_opening:
    bal:int
    acno=random.randint(1111,9999)
    acnm:str
    actyp:str
    def new_account(self):
        self.acnm=input("Enter Account holder name:")
        self.actyp=input("Enter Accoutn type:")

class deposite(ac_opening):
    dep_am:int
    def depo(self):
        self.dep_am=int(input("Enter your deposite amount:"))
        if self.dep_am>=2000:
            self.bal+=self.dep_am
        else:
            print("Error!")
       

class withdrwal(deposite):
    wit_am:int
    def withd(self):
        self.wit_am=int(input("Enter your withdrwal amount:"))
        self.bal-=self.wit_am

class statements(withdrwal):
    def final_statement(self):
        print("A/c No.:",self.acno)
        print("A/c Holder Name:",self.acnm)
        print("A/c Type:",self.actyp)
        print("Total Balance:",self.bal)

st=statements()
st.new_account()
st.depo()
st.withd()
st.final_statement()


