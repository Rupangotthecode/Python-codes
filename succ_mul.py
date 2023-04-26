n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))
sum = 0;
print(A)
for i in range(0,n-1,2):
    num1 = A[i]
    num2 = A[i+1]
    sum = sum + (num1 * num2)

print(sum)