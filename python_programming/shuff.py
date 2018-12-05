import random
list1=[2,4,5,6,'u']
d=random.shuffle(list1)
print(d)
def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i

   return theSum

print(sumOfN(10))
