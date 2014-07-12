import math

alph = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

file = open("names.txt")

el =""
temp = ""
n = 0
names = []

input = file.read()
print(len(input))

while n < len(input):
	temp = input[n]
	n += 1
	if temp == '"':
		el = el
	elif temp != ",":
		el += temp
	else:
		names.append(el)
		#print(names)
		el = ""
#
#MAX = len(names)
#names = names.split()

val = 0

prod = 0

names.sort()

for n in range(31, 61):
	print(names[n])


for n in range(0, len(names)):
	val = 0
	for k in range(1, len(names[n-1])):
		val += alph[names[n-1][k]]
	#print(n)
	prod += (val*n)
"""
n = 936
print(names[n])
val = 0
for k in range(0, len(names[n])):
	val += alph[names[n][k]]

print(val)
"""
print(len(names))
print(prod)
#print(names)
#print(names)



