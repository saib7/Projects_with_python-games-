from turtle import Turtle, Screen
import random


t = Turtle()
screen = Screen()
screen.colormode(255) #colormode is probably set to 1.0, so either the individual color coordinates need to be floats in the range 0 to 1, or we need to set the colormode to 255.
#t.color("blue")
t.pensize(10)
t.speed("fast")
#colors = ["dark blue", "dodger blue", "lime", "gold", "red", "deep pink", "maroon", "black"]
directions = [0, 90, 180, 270, 360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


for _ in range(200):
    t.color(random_color())
    t.forward(25)
    t.setheading(random.choice(directions))







screen.exitonclick()