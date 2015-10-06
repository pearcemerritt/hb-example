class Food(object):
  def __init__(self, name, color, flavor_categories):
    self.name = name
    self.color = color
    self.flavor_categories = flavor_categories

class Animal(object):
  def __init__(self, name, colors, weight):
    self.name = name
    self.colors = colors
    self.weight = weight

class Plant(object):
  def __init__(self, name, colors, family):
    self.name = name
    self.colors = colors
    self.family = family

print(Food("cake", ["white", "pink"], ["sweet", "desert"]))
print(Food("apple", ["green"], ["sweet", "tart", "fruit"]))
print(Food("orange", ["orange"], ["sweet", "fruit"]))

print(Animal("Dog", ["many"], 100))

print(Plant("rose", ["red", "pink"], "flower"))
