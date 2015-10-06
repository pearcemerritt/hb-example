class BankAccount(object):
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def deposit(self, amt):
    self.balance += amt

  def withdraw(self, amt):
    self.balance -= amt

  def print_(self):
    print "BankAccount(name:\"%s\",balance:%f)" % (self.name, self.balance)
