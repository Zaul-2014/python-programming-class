import turtle

class square():
  def __init__(self, lenght, angle):
    self.lenght = lenght
    self.angle = angle
    self.t = turtle.Turtle()

  def Draw(self):
    for i in range(4):
      self.t.forward(self.lenght)
      self.t.right(self.angle)

shape = square(100, 90)
shape.Draw()

turtle.Done()