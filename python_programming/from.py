import os
print(os.path)
def my_sort(numbers):
    odd  = [n for n in numbers if n % 2 != 0]
    even = [n for n in numbers if n % 2 == 0]
    print(sorted(odd))
    print(sorted(even))
my_sort([20,23,22,56,78,90])

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2)))

x=6
x +=4
print(x)

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)


