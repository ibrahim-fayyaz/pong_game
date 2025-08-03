from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles and ball
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score_board = Scoreboard()

# Draw the center line
center_line = Turtle()
center_line.color("white")
center_line.speed("fastest")   
center_line.penup()
center_line.pensize(5)
center_line.goto(0, -300)
center_line.setheading(90)
for _ in range(30):
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()
    center_line.forward(20)          

# Listen for key presses
screen.listen()
screen.onkeypress(r_paddle.up , "Up")
screen.onkeypress(r_paddle.down , "Down")
screen.onkeypress(l_paddle.up , "w")
screen.onkeypress(l_paddle.down , "s")

# Pause functionality
# Initialize pause state
is_paused = False
def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        screen.title("Pong Game - Paused")
    else:
        screen.title("Pong Game")
screen.onkeypress(toggle_pause, "space")

game_is_on = True
# Main game loop
while game_is_on:
    screen.update()
    if not is_paused:
        ball.move()
        #Detect collision with wall
        if abs(ball.ycor()) > 280:
            ball.bounce_y()
    
        #Detect collision with paddle
        if (ball.xcor() > 320 and ball.distance(r_paddle) < 50 and abs(ball.ycor() - r_paddle.ycor()) < 50) or \
        (ball.xcor() < -320 and ball.distance(l_paddle) < 50 and abs(ball.ycor() - l_paddle.ycor()) < 50):
            ball.bounce_x()

        #Detect Right paddle misses    
        if ball.xcor() > 380:    
            ball.reset_position()
            score_board.l_point()
        
        #Detect Left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()  
            score_board.r_point()  

    

screen.exitonclick()