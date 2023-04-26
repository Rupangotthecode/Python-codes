vowel=['a','e','i','o','u']
inp_str=input()
c=0
for i in inp_str:
    if i in vowel:
        c+=1
print(c)