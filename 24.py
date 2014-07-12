#Project Euler 24
#KMD
#Solved 25 June 2013

import itertools

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = itertools.permutations(range(10))

i = 1

for x in perms:
	if i == 1000000:
		print("The millionth permutation is:")
		for k in range(0,len(x)):
			print(x[k]),
	i += 1
	
