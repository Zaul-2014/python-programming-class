import turtle

win = turtle.Screen()
win.bgcolor('Blue')
win.title('testing canvas')
win.setup(450, 600)

arrow = turtle.Turtle()

arrow.penup()
arrow.goto(-50, 50)
arrow.pendown()


sides = 8
side_lenght = 100
angle = 360/sides

for i in range(sides):
  arrow.forward(side_lenght)
  arrow.right(angle)

turtle.done()