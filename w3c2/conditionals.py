age = int(raw_input("What's your age? "))

# if age > 18:
# 	print "Yay! I can vote!"

# if age >= 18:
# 	print "Yay! I can vote!"
# else:
# 	print "Awww, I can't vote :("

# if age >= 18 and age == 21:
# 	print "Yay! I can vote and go to a bar!"

if age >= 21:
	print "Yay! I can vote and go to a bar!"
elif age >= 18:
	print "I can vote, but I can't go to a bar"
else:
	print "I can't go to a bar or vote"

num = 8
if num % 2 == 0:
	print "the number %i is even" % num
else:
	print "the number %i is odd" % num

if num % 2 == 1:
	print "the number %i is odd" % num
else:
	print "the number %i is even" % num

num2 = 9
if num % 2 == 0 and num2 % 2 == 0:
	print "both numbers are even"
else:
	print "both numbers aren't even"

fav_color = raw_input("What's your favorite color? ")
if fav_color == "blue" or fav_color == "red" or fav_color == "yellow":
	print "my favorite color is a primary color"
else:
	print "my favorite color is not a primary color"