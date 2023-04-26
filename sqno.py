#find the no of perfect squares in the input
import math

inp_no=int(input())
c=0
for i in range(0,inp_no):
    num=int(input())
    if(math.sqrt(num)-math.isqrt(num)==0):
        c+=1
print(c)
