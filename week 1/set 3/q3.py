#Mersenneprime
def prime(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
    return 1
n=int(input("Enter number:"))
for i in range (1,n):
    if(prime(i)==1):
        for j in range (1,i):
            if(i==2**j-1):
                print(i)