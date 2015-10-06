from four_strings import four_strings

for four_string in four_strings:
  num_fours = 0
  for c in four_string:
    if c == '4':
      num_fours += 1
  if num_fours != 4:
    print '"%s" is not a valid string, it has %i 4\'s' % (four_string, num_fours)

