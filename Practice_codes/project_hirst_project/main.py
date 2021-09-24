import colorgram
from turtle import Turtle, Screen, colormode
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112), (223, 172, 184), (227, 175, 167), (103, 44, 60), (50, 56, 94), (168, 207, 185), (167, 158, 66), (60, 155, 174), (111, 122, 155), (97, 49, 44), (178, 188, 214)]
t = Turtle()
screen = Screen()
turtle.colormode(255) # for using rgb numeric colormode (1-255)
t.hideturtle() # Hiding the turtle icon
t.speed("fastest") # maximum speed of the turtle
t.penup() # stop showing line, we only visualize dots here
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_count % 10 ==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen.exitonclick()

