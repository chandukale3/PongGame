from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time as t
my_screen = Screen()
my_screen.tracer(0)
my_screen.bgcolor('black')
my_screen.setup(height=600, width=800)
my_screen.title('The Pong Game')
player1 = Paddle((350,0))
player2 = Paddle((-350,0))
ball = Ball()
scoreboard1 = Scoreboard()
scoreboard2 = Scoreboard()
scoreboard1.display1()
scoreboard2.display2()
game_over = False
while not game_over:
    t.sleep(ball.move_speed)
    my_screen.update()
    player1.move_player1()
    player2.move_player2()
    ball.move()
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.second_bounce()
    for i in range(-395,395,1):
        x_cord = i
        new_cord_top = (i,290)
        new_cord_bottom = (i,-290)
        if ball.distance(new_cord_top) < 15 or ball.distance(new_cord_bottom) < 15:
            ball.bounce()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard1.display1()
    if ball.xcor() < -400 :
        ball.reset_position()
        scoreboard2.display2()
my_screen.exitonclick()