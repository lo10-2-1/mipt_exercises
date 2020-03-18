import turtle

turtle.shape('turtle')
turtle.speed('slow')
r = 100
s = r * 3.14 / 180
# turtle.penup()
turtle.forward(r)
# turtle.pendown()
turtle.left(90)
for i in range (361):
    turtle.left(1)
    turtle.forward(s)