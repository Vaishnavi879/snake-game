import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score_board=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.update()
game_is_on=True
while(game_is_on):
    time.sleep(0.1)
    screen.update()
    snake.move()
    if(snake.head.distance(food) <17):
        food.refresh()
        score_board.scoring()
        snake.grow_length()

    if(snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300):
        # game_is_on=False
        # score_board.game_over()
        score_board.reset()
        snake.reset()

    for i in snake.snake_segments[1:]:
        if(snake.head.distance(i)<10):
            # game_is_on = False
            # score_board.game_over()
            score_board.reset()
            snake.reset()

screen.exitonclick()
