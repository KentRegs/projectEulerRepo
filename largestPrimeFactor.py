import math

num = int(input("Please enter a number: "))
lrgPrime = 0

#	'i' is considered a prime factor iff it
#	it is a factor of 'num' and if it is 
#	prime (i.e. only divisible by 1 and itself)

# 	the upper limit is the sqrt of 'num' since
# 	sqrt(num) * sqrt(num) = num. Thus, if the 
#	2 factors are equal, they are both the
#	square root of 'num'
for i in range(2, num):
	ctr = 0
	if num % i == 0:
		for j in range(2, int(math.sqrt(num))):
			if i % j == 0:
				ctr += 1
		if ctr == 1:
			if i > lrgPrime:
				lrgPrime = i
print('%d is the largest prime factor of %d' %(lrgPrime, num))