from turtle import *

tracer(0, 0)
speed(0)
setx(0)
sety(0)
seth(0)
pendown()
k = 20
l = 2
for i in range(4):
    forward(3 * k * l)
    right(90)
penup()
forward(k * l)
right(90)
forward(k * l)
pendown()
for i in range(4):
    forward(k * l)
    left(90)

penup()
for x in range(-40 * k, 40 * k, k):
    for y in range(-40 * k, 40 * k, k):
        goto(x, y)
        dot(6, "red")
update()
mainloop()
