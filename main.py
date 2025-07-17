from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width=620, height=620)
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    hit = snake.move()
    if hit == 0:
        score.reset()
        snake.restart()
    if snake.head.distance(food) < 19 :
        food.refresh()
        snake.grow_snake()
        score.score_refresh()


screen.exitonclick()
