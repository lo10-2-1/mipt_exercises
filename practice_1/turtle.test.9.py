import turtle

from numpy import sin, pi, sqrt

turtle.shape('turtle')
turtle.speed('slowest')

def eq_polygons(n, r):
    s = 2 * r * sin(pi / n)
    pol = 180 - (n - 2)/n * 180
    # turtle.left(90 + pol / 2)
    for i in range(n):
        turtle.forward(s)
        turtle.left(pol)

# turtle.penup()
# turtle.right(pol/2)
# turtle.forward(10)
# turtle.pendown()
R = 20
for i in range(3, 11):
    eq_polygons(i, (i - 2) * R)
    x = turtle.xcor()
    y = turtle.ycor()
    d = R / sqrt(2)
    turtle.goto(x - d, y - d)

# eq_polygons(3)
# eq_polygons(4)
# eq_polygons(5)
# eq_polygons(6)
# eq_polygons(7)
# eq_polygons(8)
# eq_polygons(9)
# eq_polygons(10)