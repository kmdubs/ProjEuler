maxNum = 1000
num1 = 1
num2 = 2
num = 1

i = 3


while len(str(num)) < maxNum:
	num = num1 + num2
	num1 = num2
	num2 = num
	i += 1

print("The first term in the Fibonacci sequence to contain " + str(maxNum) + " digits is: \n" + str(i))

if maxNum < 10:
	print("The number is: \n" + str (num))

