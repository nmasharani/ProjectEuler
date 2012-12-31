from sys import exit

i = 1

sumsquare = 0
squaresums = 0

while i <= 100:
	sumsquare += i * i
	squaresums += i
	i += 1

squaresums *= squaresums

print squaresums - sumsquare


