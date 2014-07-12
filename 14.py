def seq(num):
	count = 1
	while num != 1:
		if num % 2 == 0:
			num = num/2
		else:
			num = 3*num+1
		count += 1
	return count


num = []

i = 0
while i < 1000000:
	num.append(i+1)
	i += 1

maxChain = 0
chainNum = 0

chain = 0
for x in num:
	if x % 1000 == 0:
		print x
	chain = seq(x)
	if chain > maxChain:
		maxChain = chain
		chainNum = x


print "The longest chain has " + str(maxChain) + " number of chars."
print "The starting number was: " + str(chainNum)
