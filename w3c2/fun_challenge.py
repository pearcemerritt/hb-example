def do_twice(function):
	function()
	function()

def do_twice_with_value(function, value):
	function(value)
	function(value)

def print_spam():
	print 'spam'

def print_slang(phrase):
	print phrase, ', yo!'

def print_s(s):
	print s

def do_four(f, v):
	do_twice_with_value(f, v)
	do_twice_with_value(f, v)

do_twice(print_spam)
do_twice_with_value(print_slang, 'what\'s my purpose')
do_twice_with_value(print_s, 'spam')
print '********'
do_four(print_s, 'spam')