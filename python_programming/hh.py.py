
from sys import stdin
import json
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)
print(json.dumps(my_mapping, indent=4, sort_keys=True))
for _ in range(int(stdin.readline())):
    a,b,c=map(int,stdin.readline().split())
    print("Yes" if a+b>c else "No")
