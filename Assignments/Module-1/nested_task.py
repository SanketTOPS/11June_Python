a=int(input("Enter A:"))
b=int(input("Enter B:"))

if a!=0 and b!=0:
    if a>b:
        print("Mul:",a*b)
    else:
        print("Sub:",a-b)
else:
    print("Error!Invalid Number...")