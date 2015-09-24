def larger(a, b):
	if a > b:
		return a
	else: return b

print larger(4, 8)
print larger(4234*42, 634*23)
print larger(larger(4, 63), 32)

def smaller(a, b):
	if a < b: return a
	else: return b

print smaller(3.14, 6.)
print smaller(True, False)
print smaller(smaller(4,63),32)