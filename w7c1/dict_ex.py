# #1
# a
my_stats = { "name": "Pearce", "age": 25, "height": 72}
print "%s is %i years old with a height of %i" % (my_stats["name"], my_stats["age"], my_stats["height"])
# b
del my_stats["age"]
print my_stats
print

# #2
vocab_words = { "conditionals": "ifs", "iteration": "loops", "variables": "my_whatevs", "encapsulation": "functions" }
print vocab_words
print

# #3
name_chars = {}
for c in "pearce bowdon merritt":
  if c == ' ':
    continue
  if c in name_chars:
    name_chars[c] += 1
  else:
    name_chars[c] = 1
print name_chars
print

# #4
def count_letters(content):
  name_chars = {}

  for c in content:
    if c == ' ':
      continue
    if c in name_chars:
      name_chars[c] += 1
    else:
      name_chars[c] = 1

  return name_chars

print name_chars
print

# #5
f = open('one_fish_two_fish.txt')
content = f.read()
print count_letters(content)
print

# #6
def count_words(content):
  lines = content.split('\n')
  words = []
  for line in lines:
    words.extend( line.split(' ') )

  # words = content.split(' ')
  num_words = {}
  
  for word in words:
    if word in num_words:
      num_words[word] += 1
    else:
      num_words[word] = 1

  return num_words

print count_words('one fish two fish red fish blue fish')
print

# #7
f = open('one_fish_two_fish.txt')
content = f.read()
print count_words(content)
print

# #8
d = {'orange': 1.5, 'pear': 3, 'banana': 4, 'apple': 2}
def most_exp(d):
  most_exp_num = -999999999
  most_exp_name = ''
  for key, value in d.items():
    if value > most_exp_num:
      most_exp_name = key
      most_exp_num = value
  return most_exp_name
print "%s is the most expensive out of %r" % (most_exp(d), d)
