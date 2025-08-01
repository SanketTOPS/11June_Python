class master:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)
    
    def production(self,x,y):
        print("Production:",x*y)

class home(master):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)
    
    def production(self, x, y):
        return super().production(x, y)

class about(master):
    def getdata(self, id, name):
        return super().getdata(id, name)
    
    def production(self, x, y):
        return super().production(x, y)
   

h=home()
h.getdata(101,'Sanket')
h.production(32,56)

a=about()
a.getdata(102,'Ashok')
a.production(45,7)