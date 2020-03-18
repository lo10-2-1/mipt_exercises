import turtle

turtle.shape('turtle')
# turtle.speed('slow')
s = 1
rot = 180

# x = 0
# y = 0
# d = 3
# for i in range(100):
#     x += d
#     y += d
#     turtle.goto(x,y)

for i in range (1000):
    turtle.left(rot)
    turtle.forward(s)
    rot = rot - rot/360