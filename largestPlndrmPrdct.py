# #	manual solution

# lrgPlndrm = 0

# def isPlndrm(result):
# 	temp = result
# 	rev = 0

# 	for i in range(len(str(result)), 0, -1):
# 		mdfr = temp % 10
# 		rev += mdfr * (10 ** (i - 1))
# 		temp /= 10

# 	if result == rev:
# 		return 1

# num1 = 100
# num2 = 1000

# for i in range(num1, num2):
# 	for j in range(num1, num2):
# 		product = i * j
# 		print('i = %d and j = %d' %(i, j))
# 		if isPlndrm(product):
# 			print('product = %d' %product)
# 			if product > lrgPlndrm:
# 				lrgPlndrm = product
# print('largest palindrome product = %d\n' %lrgPlndrm)

# Python solution

from itertools import product

lrgPlndrm = 0
num1 = 100
num2 = 1000


for i in range(num1, num2):
	for j in range(num1, num2):
		product = i * j
		print('i = %d and j = %d' % (i, j))
		if str(product) == str(product)[::-1]:
			print('product = %d' % product)
			if product > lrgPlndrm:
				lrgPlndrm = product
print('\nlargest palindrome product = %d' % lrgPlndrm)
