import turtle

turtle.shape('turtle')
turtle.speed('slow')
fr = 100
n = 12
rot = 360 / n + 360
turtle.right(360 / n)
for i in range (n):
    turtle.forward(fr)
    turtle.stamp()
    turtle.back(fr)
    turtle.right(rot)