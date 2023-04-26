#tutionnoter
ttn=10000
rate=5
time=10
for i in range(0,10):
    ttn=float(ttn+(0.05*ttn))
print("tution after 10years=",ttn)
sum=0
for i in range (0,4):
    sum=sum+ttn
    ttn=float(ttn+(0.05*ttn))
print("Tution 4 yrs hence=",sum)
