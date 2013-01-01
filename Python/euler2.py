prev = 1
cur = 2
sum = 0

while prev < 4000000:
	cur = cur + prev
	prev = cur - prev
	if prev % 2 == 0:
		sum += prev

print sum


