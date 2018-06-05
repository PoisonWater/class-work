import turtle
import math
tt = turtle.Turtle()
pi = math.pi

a = list(range(360))

while True:
    for i in a:
        tt.forward(1)
        tt.left(1)
    tt.forward(360/pi)