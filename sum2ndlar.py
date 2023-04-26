def LargeSmallSum(arr):
    even=[]
    odd=[]
    for i in range(0,len(arr),2):
        even.append(arr[i])
    for i in range(1,len(arr),2):
        odd.append(arr[i])
    even.sort()
    odd.sort()
    sum=even[len(even)-2]+odd[1]
    return sum

arr=[1,2,3,4,5,6,7,8,9]
result=LargeSmallSum(arr)
print(result)
s='IOOKM'
print(s.isupper())
if(s.isupper()):   
    print('o') 
    result=s.lower()
print(result)