
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

print(len(months))

sun = 0

dM = 1
dW = 3
m = 1
Y = 1901

endY = 2000

dW = (dW + 5) % 7
dM = (dM + 5)

while Y <= endY:
	print(Y)
	m = 1
	while m <= len(months):
		dM += 7
		if Y % 4 == 0 and m == 2:
			if dM > months[m] + 1:
				dM = dM - (months[m] + 1)
				m+=1
		elif dM > months[m]:
			dM = dM - months[m]
			m += 1
#		print("Month is: " + str(m) + "   Day is: " + str(dM))
		if dM == 1:
			sun += 1
#			print("Sum is: " + str(sun))
	Y += 1

print(sun)
