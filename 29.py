import math

MAX = 100

a = range(2,MAX+1)
b = range(2,MAX+1)

prod = []

for i in range(2,MAX+1):
	for m in range(2,MAX+1):
		n = i ** m
		prod.append(n)

prod.sort()
rem = []
for i in range(1,len(prod)):
	if prod[i] == prod[i-1]:
		rem.append(i)

for i in range(len(rem)):
	prod.pop(rem[i])

print(len(prod))

