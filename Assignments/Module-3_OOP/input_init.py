class studinfo:
    def __init__(self):
        unm=input("Enter your Username:")
        pas=input("Enter your Password:")

        if unm=='admin' and pas=='admin':
            print("Login Successfull!")
        else:
            print("Error!Invalid Username or Password...")

st=studinfo()