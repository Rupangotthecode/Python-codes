n=int(input())
m=int(input())
num=0
for i in range(n,n+15):
    if(i%15==0):
        num=i
        break
for i in range(num,m+1,15):
    print(i)
    
