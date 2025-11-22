import turtle

win = turtle.Screen()
win.bgcolor('light blue')
win.screensize(500, 500)

arrow = turtle.Turtle()

radius1 = 100
radius2 = 200

for i in range(radius1):
  arrow.right(1)
  arrow.forward(1)

for i in range(radius2):
  arrow.left(1)
  arrow.backward(1)

turtle.done()