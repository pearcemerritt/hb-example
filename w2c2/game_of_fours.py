import math
from four_strings import four_strings

f = math.factorial

for number_string in four_strings:
	print "%i = %s" % (eval(number_string), number_string)
