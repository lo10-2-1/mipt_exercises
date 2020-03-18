import turtle

turtle.shape('turtle')
turtle.speed('fast')

r = 50
s = r * 3.14 / 180

def circle():
    for i in range (361):
        turtle.left(1)
        turtle.forward(s)
    for i in range (361):
        turtle.right(1)
        turtle.forward(s)
    turtle.left(60)

circle()
circle()
circle()