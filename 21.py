#Project Euler No. 21
#KMD
#18 June 2013

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

num = 5.0
div = 2.0
temp = 0

MULTS = []
SUM = dict()
AMPAIR = []

SUM[1] = 1
SUM[2] = 3
SUM[3] = 4
SUM[4] = 7

MAX = 10000
#num = 219.0

while num <= MAX:
	MULTS.append(1.0)
	while div <= (num/2.0):
		if num % div == 0:
			MULTS.append(div)
 		div += 1.0
	SUM[num] = sum(MULTS)
	div = 2.0
	num += 1.0
	MULTS = []

#print(SUM)

#print(SUM[220.0])
#print(SUM[284.0])

for num in range(2,MAX+1):
	if SUM[num] <= MAX:
		if SUM[SUM[num]] == num and SUM[num] != num:
			AMPAIR.append(num)

print("The amicable pairs under "+str(MAX) + " are: " + str(AMPAIR))
print("The sum of all amicable pairs under " + str(MAX) + " is: " + str(sum(AMPAIR)))



