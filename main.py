import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = []

for i in range(0, 3):
    new_section = Turtle(shape='square')
    new_section.penup()
    new_section.color('white')
    new_section.goto(x=(i*-20), y=0)
    snake.append(new_section)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(x=new_x, y=new_y)
    snake[0].forward(20)













screen.exitonclick()
