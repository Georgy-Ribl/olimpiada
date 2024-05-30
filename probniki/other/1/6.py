from turtle import *

speed(0)
tracer(0)
setx(0)
sety(0)
k = 17
for i in range(8):
    forward(12 * k)
    left(45)
penup()
left(90)
forward(23 * k)
pendown()
for i in range(4):
    forward(58 * k)
    right(90)

penup()
for x in range(-60 * k, 60 * k, k):
    for y in range(-60 * k, 60 * k, k):
        goto(x, y)
        dot(4, 'blue')

update()
mainloop()
