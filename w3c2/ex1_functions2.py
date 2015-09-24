def add(a, b): return a + b
def subtract(a, b): return a-b
def multiply(a, b): return a*b
def divide(a, b): return a/b
def mod(a, b): return a%b
def sq(a): return a**2

# Write the code for the following inside of the ~/intro_class/calculator.py file.
# 1. Set a variable called age to add(30,4)
age = add(30, 4)
# 2. Set a variable called height to subtract(78, 2)
height = subtract(78, 2)
# 3. Set a variable called weight to multiply(6,24)
weight = multiply(6,24)
# 4. Set a variable called iq to divide(100,2)
iq = divide(100,2)
# 5. print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# More survey stuff
name = raw_input("What's your name? ")
color = raw_input("What's your favorite color? ")
hobby = raw_input("What's your favorite hobby? ")
movie = raw_input("What's your favorite movie? ")

def print_survey_results(name, color, hobby, movie):
	print "%s's favorite color is %s" % (name, color)
	print "%s's favorite hobby is %s" % (name, hobby)
	print "%s's favorite movie is %s" % (name, movie)

print_survey_results(name, color, hobby, movie)
