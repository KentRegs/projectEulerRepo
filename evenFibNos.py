past = 0
prst = 1
ctr = 0
res = 0
temp = 0

while temp < 4000000:
	temp = past + prst
	past = prst
	prst = temp
	print(temp)

	if temp < 4000000 and temp % 2 == 0:
		res = res + temp

print('res = ' + str(res))


