for i in range(1,21):
	print i,

print

for i in range(1,21):
	if i == 13:
		print 'hello',
	else:
		print i,

print

for i in range(0, 101, 10):
	print i,

print

for i in range(11):
	if i % 2 == 1:
		print i,

print

for i in range(10, -1, -1):
	print i,

print

for i in range(10, 0, -1):
	print i,
print "Blastoff!"

fruits = ['apples', 'oranges', 'bananas']
print
for fruit in fruits:
	print fruit,
print

for i in range(len(fruits)):
	print fruits[i],
print

def sum_nums(num):
	sum = 0
	for i in range(num):
		sum += i
	return sum

print sum_nums(3)
		
def sum_nums11(num):
	sum = 0
	for i in range(num + 1):
		sum += i
	return sum

print sum_nums11(3)

def sum_nums2(num):
	sum = 0
	if num < 0:
		for i in range(num, 0):
			sum += i
	else:
		for i in range(num + 1):
			sum += i
	return sum

print sum_nums2(-3)
print sum_nums2(3)

def fizz_buzz(num):
	for i in range(1, num+1):
		if i % 5 == 0 and i % 3 == 0:
			print "FIZZBUZZ"
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"
		else:
			print i

fizz_buzz(50)
