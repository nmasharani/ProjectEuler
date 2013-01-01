from sys import exit

def multiply(n):
	i = 0
	prod = 1
	while i < len(n):
		prod *= int(n[i])
		i += 1
	
	return prod


f = open('bignum.txt','r')
number = f.read()
f.close()

length = len(number)

i = 0
max = 0
while i + 5 < length:
	num = number[i:i+5]
	mult = multiply(num)
	if mult > max:
		max = mult
	i += 1

print max
