import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# TODO: 1. Create the screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Pong Game")
game_screen.tracer(0)

# TODO: 2. Create and move a paddle
paddle_r = Paddle((350, 0))
# TODO: 3. Create another paddle
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_screen.listen()
game_screen.onkey(paddle_r.up, "Up")
game_screen.onkey(paddle_r.down, "Down")
game_screen.onkey(paddle_l.up, "w")
game_screen.onkey(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    game_screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    # TODO: 5. Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO: 6. Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_refresh()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.ball_refresh()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
    # TODO: 5. Detect when paddle misses

# TODO: 6. Keep Score

game_screen.exitonclick()
