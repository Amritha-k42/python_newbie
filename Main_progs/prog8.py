#number greater or what?

a = int(input("Enter 1st nnumber: "))
b = int(input("Enter 2nd nnumber: "))
c = int(input("Enter 3rd nnumber: "))

if(a>=b and a>=c):
    print("1st number is largest->", a)
elif(b>=c):
    print("2nd number is the largest->", b)
else:
    print("3rd number is the largest->", c)