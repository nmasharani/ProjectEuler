from math import sqrt
from math import trunc
from sys import exit

def isprime(num):
	root = trunc(sqrt(num)) + 1
	i = 2
	while i < root:
		if num % i == 0:
			return False
		i += 1
	return True

number = 600851475143

root = trunc(sqrt(number)) + 1

i = root
while i > 1:
	if number % i == 0:
		if isprime(i):
			print i 
			exit(0)
	i -= 1
