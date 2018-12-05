a=int(input("please enter the value of first range"))
b=int(input("please enter the value of the second range"))
for k in range(a,b):
    if all(k%r!=0 for r in range(2,k)):
        print(k)
    
    
