import math

def tanhFuntion(data):
	result = []
	for x in data:
		tam = (2/(1+math.exp(-2*x))-1)
		result.append(tam)
	return result

data = [1, 5, -4, 3, -2]

print(tanhFuntion(data))