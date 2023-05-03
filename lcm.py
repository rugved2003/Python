a=3
b=6
lcm=0
if a>b: #False
    max=a
else: #True
    max=b # max=6
    #print(max)
while((max%a==0)and(max%b==0)): # (6%3)=0, (6%6)=0
    lcm=max
    print(lcm)
    break