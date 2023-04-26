#sum==0
class Solution:
    array=[]*100
    n=0
    def __init__(self,n):
        self.n=n
    def sol(self):
        resarr=[]
        for i in range(0,self.n):
            for j in range(i,self.n):
                if(self.array[i]+self.array[j]==0):
                    resarr.append([self.array[i],self.array[j]])
        return resarr
    def inputEl(self):
        for i in range(0,self.n):
            num=int(input("Enter Element:"))  
            self.array.append(num)
s1=Solution(7) 
s1.inputEl()
res=[]
res=s1.sol()   
print(res)
    
        

