class rectangle():
  def __init__(self, L, W):
    self.L = L
    self.W = W

  def area(self):
    return self.L * self.W
  
shape = rectangle(25, 90)
print('area of shape: ', shape.area(), 'm\u00B2')