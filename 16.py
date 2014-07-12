
prod = str(pow(2,1000))
print len(prod)

i = 0
temp = 0
sol = 0
while i < len(prod):
	temp = int(prod[i])
	sol += temp
	i += 1

print sol
