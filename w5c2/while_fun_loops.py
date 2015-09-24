i = 1
while i <= 20:
	print i,
	i += 1
print

i = 1
while i <= 20:
	if i == 13:
		print "hello",
	else:
		print i,
	i += 1
print

i = 0
while i <= 100:
	print i,
	i += 10
print

i = 0
while i <= 10:
	if i % 2 == 1:
		print i,
	i += 1
print

i = 10
while i >= 0:
	print i,
	i -= 1
print

i = 10
while i > 0:
	print i,
	i -= 1
print "Blastoff!"

fruits = ['apples', 'oranges', 'bananas']
i = 0
while i < len(fruits):
	print fruits[i],
	i+=1
print

def sum_nums(num):
	sum = 0
	i = 0
	while i < num:
		sum += i
		i += 1
	return sum
print sum_nums(3)

def sum_nums11(num):
	sum = 0
	i = 0
	while i <= num:
		sum += i
		i += 1
	return sum
print sum_nums11(3)

def sum_nums2(num):
	sum = 0
	if num < 0:
		i = num
		while i <= 0:
			sum += i
			i += 1
	else:
		i = 0
		while i <= num:
			sum += i
			i += 1
	return sum
print sum_nums2(-3)
print sum_nums2(3)

def fizz_buzz(num):
	i = 1
	while i <= num:
		if i % 5 == 0 and i % 3 == 0:
			print "FIZZBUZZ"
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"
		else:
			print i
		i += 1

fizz_buzz(50)
