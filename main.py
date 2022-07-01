from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = []

for i in range(0, 3):
    new_section = Turtle(shape='square')
    new_section.penup()
    new_section.color('white')
    new_section.goto(x=(i*-20), y=0)
    snake.append(new_section)













screen.exitonclick()
