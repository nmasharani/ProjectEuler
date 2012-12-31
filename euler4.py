# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from sys import exit

def reverseNum(num):
	strng = (str(num))[::-1]
	#print strng
	return int(strng)


left, right = 999, 999 
numbers = []

while left > 99:
	while right > 99:
		product = left * right
		reverse = reverseNum(product)
		if product == reverse:
			numbers.append(product)
	
		right -= 1
	left -= 1
	right = 999

numbers.sort()
index = len(numbers) - 1
print numbers[index]
