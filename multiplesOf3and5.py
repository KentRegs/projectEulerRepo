res = 0
n = 999

while n > 0:
	if n % 3 == 0 or n % 5 == 0:
		print('n = ' + str(n))
		res += n
	n = n - 1

print('res = ' + str(res))