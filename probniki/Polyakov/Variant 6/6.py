from turtle import *

tracer(0)
speed(0)
update()
setx(0)
sety(0)
seth(90)

k = 20

for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
penup()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
pendown()
for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        goto(x, y)
        dot(4, 'blue')

update()
mainloop()
