# Complex multiplication

def cm0(a,b,c,d):
	return a*c-b*d, b*c+a*d

def cm1(a,b,c,d):
	ac, bd, tsum = a*c, b*d, (a+b)*(c+d)
	return ac-bd, tsum-ac-bd

if __name__ == '__main__':
	print(cm1(0,1,0,1))
	print(cm1(4,3,-4,3))
	print(cm1(3,4,-4,-3))
