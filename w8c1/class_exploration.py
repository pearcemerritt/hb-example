class Yo(object):
  dogg = 'duuuuude'

  def __init__(self, sup):
    self.sup = sup

  def getSup(self):
    return self.sup

  def setSup(self, sup):
    self.sup = sup

  def getAw(self):
    return self.aw

  def setAw(self, aw):
    self.aw = aw

  def getDogg():
    return Yo.dogg

y = Yo("heyo")
print y.getSup()
y.setSup("oi!")
print y.getSup()
# print y.getAw()
y.setAw('snap')
print y.getAw()
print Yo.dogg
print Yo.getDogg()
