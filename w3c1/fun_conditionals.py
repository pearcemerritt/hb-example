def check_for_string(input):
	if (type(input) == str):
		print "%s a string!" % (input)
	else:
		print "%s is not a string" % (input)

print "using 8"
check_for_string(8)
print "using 'hello'"
check_for_string("hello")
