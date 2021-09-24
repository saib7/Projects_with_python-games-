from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle Will Win The Race? Enter a Color: ")
colors = ["red", "orange", "blue", "green", "purple", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} is the winner.")
            else:
                print(f"You've lost. the {winning_color} is the winner.")
        rand_distance = random.randint(0, 11)
        turtle.forward(rand_distance)







screen.exitonclick()