import turtle

turtle.shape('turtle')
turtle.speed('fastest')

turtle.left(90)

def face():
    r = 50
    s = r * 3.14 / 180
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    for i in range(361):
        turtle.left(1)
        turtle.forward(s)
    turtle.end_fill()

face()