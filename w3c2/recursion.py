def countdown(count):
	if (count == 0):
		print "Blastoff!"
	else:
		print count
		countdown(count-1)

countdown(5)
countdown(10)


def countup(count):
	if (count == 1):
		print count
	else:
		countup(count - 1)
		print count

countup(5)
countup(10)
