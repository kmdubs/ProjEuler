#Project Euler Problem 17
#KMD
#Solved 22 June 2013

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
tens = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

LENGTH = 0
MAX = 1000

N = 105

#print(str(N % 10))
#print(str((N - (N / 100)) / 10))
#print(str(N / 100) + str((N - (N / 100)*100)))


#print(342/100)
#print(((342-(342/100)*100))/10)#-(((342-(342/100)*100))/10))
#print((((342-(342/100)*100))%10))

#ARR = [115]

for num in range(1, MAX+1):
#for num in ARR:
	if len(str(num)) == 1:
#		print(str(ones[num]))
		LENGTH += len(str(ones[num]))
	elif len(str(num)) == 2:
		if num / 10 == 1:
#			print(str(teens[num]))
			LENGTH += len(str(teens[num]))
		elif num % 10 == 0:
#			print(str(tens[num]))
			LENGTH += len(str(tens[num]))
		else:
#			print(str(tens[num - (num % 10)]) + str(ones[num % 10]))
			LENGTH += len(str(tens[num - (num % 10)])) + len(str(ones[num % 10]))
	elif len(str(num)) == 3:
		#print(num / 100)
		#print((num - (num / 100)) / 10)
		#print((num - (num / 100) * 100))
		if num % 100 == 0:
			print(str(ones[num / 100]) + "hundred")
			LENGTH += len(str(ones[num / 100]) + "hundred")
		elif ((num - (num / 100) * 100) % 10) == 0:
			if (num - (num / 100) * 100) == 10:
#				print(str(ones[num / 100]) + "hundredand" + str(teens[(num - (num / 100) * 100)]))
				LENGTH += len(str(ones[num / 100]) + "hundredand" + str(teens[(num - (num / 100) * 100)]))
			else:
#				print(str(ones[num / 100]) + "hundredand" + str(tens[(num - (num / 100) * 100)]))
				LENGTH += len(str(ones[num / 100]) + "hundredand" + str(tens[(num - (num / 100) * 100)]))
		elif ((num-(num / 100) * 100)) < 10:
#			print(str(ones[num / 100]) + "hundredand" + str(ones[(num-(num/100)*100)]))
			LENGTH += len(str(ones[num / 100]) + "hundredand" + str(ones[(num-(num/100)*100)]))
		elif ((num-(num / 100) * 100)) < 20 and ((num-(num / 100) * 100)) > 10 :
#			print(str(ones[num / 100]) + "hundredand" + str(teens[(num-(num/100)*100)]))
			LENGTH += len(str(ones[num / 100]) + "hundredand" + str(teens[(num-(num/100)*100)]))
		elif (num - (num / 100)) / 10 != 1:
#			print(str(ones[num / 100]) + "hundredand" + str(tens[((num - (num / 100)*100) / 10) * 10])) + str(ones[(num - (num / 100)*100) % 10])
			LENGTH += len(str(ones[num / 100]) + "hundredand" + str(tens[((num - (num / 100)*100) / 10) * 10]) + str(ones[(num - (num / 100)*100) % 10]))

LENGTH += len("onethousand")
print(LENGTH)


