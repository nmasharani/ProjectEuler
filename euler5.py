from sys import exit

def modtest(n):
	if n % 19 != 0:
		return False
	if n % 18 != 0:
		return False
	if n % 17 != 0:
		return False
	if n % 16 != 0:
		return False
	if n % 15 != 0:
		return False
	if n % 14 != 0:
		return False
	if n % 13 != 0:
		return False
	if n % 12 != 0:
		return False
	if n % 11 != 0:
		return False
	return True

i = 2520

while True:
	i += 20
	if modtest(i):
		print i
		exit(0)
