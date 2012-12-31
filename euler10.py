import math
from sys import exit

def IsPrime(n):
	if n % 2 == 0: 
		return False
	i = 3
	while i < int(math.sqrt(n)) + 1:
		if n % i == 0:
			return False
		i += 2
	return True

sum = 2
i = 3
while i < 2000000:
	if IsPrime(i):
		sum += i
	i += 2

print sum

