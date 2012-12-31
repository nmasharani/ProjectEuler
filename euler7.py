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

count = 1
num = 3

while count < 10001:
	if IsPrime(num):
		count += 1
		if count == 10001:
			print num
	num += 2

