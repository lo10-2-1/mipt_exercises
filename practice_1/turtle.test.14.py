import turtle

turtle.shape('turtle')
turtle.speed('slowest')

def stars(n):
    s = 100
    cor = 360 - (n - 2)/n * 180 * 2
    turtle.penup()
    turtle.forward(s)
    turtle.left(180)
    turtle.pendown()
    for i in range(n):
        turtle.forward(s)
        turtle.left(cor)

stars(5)
stars(11)