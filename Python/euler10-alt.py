# Uses a sieve of eratosthenes
sieve = [0] * 2000000

num = 2
sum = 0

while num < 2000000:
	if sieve[num] == 0:
		sum += num
		temp = num
		while temp < 2000000:
			sieve[temp] = 1
			temp += num
	num += 1

print sum
