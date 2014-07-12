#Project Euler Problem 10
#KMD
#Solved 20 June 2013

def isPrime(num):
	prime = True
	if num == 1 or num == 4:
		prime = False
	elif num == 2 or num == 3:
		prime = True
	
	if num % 2 == 0 and num != 2:
		prime = False

	n = 3  
	while prime == True and n < num / 2.0:  
		if num % n == 0 and n != num:  
			prime =  False
		n += 1
	return prime
	

primes = []

MAX = 2000000

for n in range(1,MAX+1):
	#print n
	if n == 1:
		print "[#",
	elif n % 100000 == 0:
		print "#",
	elif n == MAX:
		print "#]"
		print "DONE!"
	#print("num = " + str(n) + "  " + str(isPrime(n)))
	if isPrime(n):
		primes.append(n)

#print(primes)

"""
while n < MAX_NUM:
	arrays.append(n+1)
	n += 1

print "array done"
primes = []
num = 1
i = 0
total = 0

while i < len(arrays):
	if i % 10000 == 0:
		print i/10000
	elif i == 0:
		print 0

	if isPrime(arrays[i]):
		primes.append(arrays[i])
		total += arrays[i]
	i += 1	

print total
print "primes set. Largest prime is: " + primes(len(primes)-1) + "\nNumber of primes is: " + len(primes)
"""
SUM = sum(primes)	

print SUM
