#Problem set 1
#Name Madhavi Desai
#Time 12:20PM

from math import *

nextOdd = 3
numList = []
primeList = []
divisior = 1
countDivisior = 0
primeCount = 0
column_pad = 6
max_column = 5
column = 1
logSum = 0

noOfPrime = input('Enter max range for prime numbers: ')

#Create an array of odd numbers from 1 to 10000
while(nextOdd < noOfPrime):
	if(nextOdd%2 != 0):
		numList.append(nextOdd)
	nextOdd = nextOdd + 1

#Initialize n with first number from odd numbers list.	
n = numList[0]

#Since we know that 2 is prime number, add it to primeList array.
primeList.append(2)
print str(2).center(column_pad),

for n in numList:
	#Find number of divisiors for number n.
	while(divisior <= n):
		if(n%divisior == 0):
			countDivisior = countDivisior + 1
		divisior = divisior + 1
	
	#If there are only 2 divisiors for number n then it is 
	#prime number and add it to the primeList array.	
	if(countDivisior == 2):
		primeList.append(n)
		print str(n).center(column_pad),
		column += 1
		if column == max_column:
			print
			column = 1
		primeCount = primeCount + 1
		lastPrime = n
	divisior = 1
	countDivisior = 0
	if (primeCount == 999):
		break
print
print "10th prime number is",lastPrime
for i in primeList:
	logSum = logSum + log(i)

print "The sum of log of",len(primeList),"prime numbers is",logSum
print "The ratio of",logSum, "and",len(primeList),"is",logSum/len(primeList)