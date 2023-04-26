#pythagorean triplet
def pytha(a,b,c):
    if((a*a+b*b)==c*c):
        print("It is a pythagorean triplet")
    else:
        print("It is not a pythagorean triplet.")

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))

pytha(a,b,c)