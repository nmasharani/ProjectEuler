import math
from sys import exit

def Triple(one, two):
	three = math.sqrt(one * one + two * two)
	if int(three) == three:
		return three
	return -1

def SumThousand(one, two, three):
	return one + two + three == 1000

for i in range(1,1000):
	for j in range(1,1000):
		k = Triple(i,j)
		if k != -1 and SumThousand(i,j,k):
			print i * j * k
			exit(0)

