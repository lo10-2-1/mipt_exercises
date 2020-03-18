import turtle

turtle.shape('turtle')
turtle.speed('fastest')

turtle.left(90)

def circle(r):
    s = r * 3.14 / 180
    for i in range (361):
        turtle.left(1)
        turtle.forward(s)
    for i in range (361):
        turtle.right(1)
        turtle.forward(s)

circle(10)
circle(15)
circle(20)
circle(25)
circle(30)
circle(35)