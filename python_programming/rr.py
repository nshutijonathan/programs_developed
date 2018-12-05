firstrange=int(input("please enter your first  number"))
lastrange=int(input("please enter your last number"))
sum=0
for m in range(firstrange,lastrange+1):
    if m%9==0:
        sum=sum+m
print(sum)
