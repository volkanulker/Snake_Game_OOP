from scoreboard import ScoreBoard
from turtle import Screen , Turtle, position
import random
import time
from snake import Snake
from food import Food

screen = Screen()

screen.setup(width=600 , height=600)

screen.bgcolor("black")

screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()

food = Food()

score_board = ScoreBoard()

screen.listen()




game_is_on = True


screen.update()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        score_board.refresh_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    
    # Detect collision with tail.
    # if head collides with any segment in tail:
        # trigger game over sequence

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            score_board.game_over()
    
   

screen.exitonclick()