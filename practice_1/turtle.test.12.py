import turtle

turtle.shape('turtle')
turtle.speed('fastest')

turtle.left(90)

def circle():
    r = 50
    s = r * 3.14 / 180
    for i in range (179):
        turtle.right(1)
        turtle.forward(s)
    for i in range (181):
        turtle.right(1)
        turtle.forward(s/5)

circle()
circle()
circle()
circle()
circle()