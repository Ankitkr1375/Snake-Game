from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
# we will user tracer to stop the abnormal behaviour
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()#updating the screen before iterating in for loop
    time.sleep(0.09)#keeping it to 0.1 for smoother operation
    snake.move()
    # detect colloison with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # detect colloison with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect colloison with taIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False   
            scoreboard.game_over()



screen.exitonclick()