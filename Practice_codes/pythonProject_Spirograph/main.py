import random
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed('fastest')

def random_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        current_heading = t.heading() # current position of the circle.
        t.setheading(current_heading + size_of_gap)

draw_spirograph(1)







screen.exitonclick()