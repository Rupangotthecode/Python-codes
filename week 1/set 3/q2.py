#twinprimes
def prime(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
    return 1

for i in range(2,100):
    if(prime(i)==1):
        if(prime(i+2)==1):
            print(i,i+2)
        