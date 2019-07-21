import math

def sigMold(data):
	result = []

	for i in data:
		a = 1 / (1+math.exp(-i))
		result.append(a)
	return result

data = [1, 5, -4, 3, 2]

print(sigMold(data))