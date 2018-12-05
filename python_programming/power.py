def power(x,y):
	if y == 0:
		return 1
	else:
		return (x*(power(x, y-1)))
f=int(input("please enter the first number"))
l=int(input("please enter the second number"))	    
power(f,l)
