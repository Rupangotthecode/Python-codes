#input a string and print elements in alphabetic order
inp_str=input()
inp_str.lower()
res=inp_str.split(' ')
res.sort()
print(res)