from turtle import Turtle, Screen

t = Turtle()
t.color("blue")
import random
colors = ["dark blue", "dodger blue", "lime", "gold", "red", "deep pink", "maroon", "black"]

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        t.forward(105)
        t.left(angle)

for shape_side_n in range(3,10):
    t.color(random.choice(colors))
    draw_shapes(shape_side_n)










screen = Screen()
screen.exitonclick()