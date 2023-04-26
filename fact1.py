#if one present in factorial,print yes else no
num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
res=str(fact)
if '1' in res:
    print('yes')
else:
    print('no')