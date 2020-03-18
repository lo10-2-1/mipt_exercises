import turtle

turtle.shape('turtle')
turtle.speed('slowest')
fr = 10
d = 10
x = 0
y = 0
for i in range (11):
    turtle.forward(fr)
    turtle.left(90)
    turtle.forward(fr)
    turtle.left(90)
    turtle.forward(fr)
    turtle.left(90)
    turtle.forward(fr)
    turtle.left(90)
    turtle.penup()
    y -= d / 2
    x -= d / 2
    turtle.goto(x, y)
    turtle.pendown()
    fr += d