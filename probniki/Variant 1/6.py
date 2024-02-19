from turtle import *

tracer(0, 0)
speed(0)
setx(0)
sety(0)
pendown()
k = 40
for i in range(4):
    forward(12 * k)
    right(90)
for i in range(3):
    forward(12 * k)
    right(120)
penup()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(6, "red")
update()
mainloop()
