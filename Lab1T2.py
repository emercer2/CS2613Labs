import math

def absolute(num):
	if(num < 0):
		return num*(-1)
	else:
		return num
	

def formula(a, b):
	result = math.sqrt(absolute(((a-1)**5)-absolute(b+1)))
	return result
	
while(True):	
	print("Input two values:")

	a = input()
	b = input()
	if(a == "X"):
		break
	result = formula(float(a), float(b))
	print("Result: " +  str(result))

