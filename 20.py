import math

ans = math.factorial(100)

temp = str(ans)

total = 0
i = 0
while i < len(temp):
	total += int(temp[i])
	i += 1
print temp
print total
