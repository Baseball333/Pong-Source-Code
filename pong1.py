# Pong variant
# Commit 1

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=400)

# Score
score_a = 0
score_a = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed = 0
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("blue")
ball2.penup()
ball2.dx = -2
ball2.dy = -2

# Ball 3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("blue")
ball3.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Ball 4
ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("blue")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = -1
ball4.dy

balls = [ball1, ball2, ball3, ball4]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# Gameplay Functions
def paddle_a_up():
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y += 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    

# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Down")
wn.onkeypress(paddle_b_dpwn, "Down")

# Main gameplay
while True:
    wn.update()
    
    for ball in balls:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
     if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")
            
     if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.write("Playee A: {} Player B: {}" align="center", font="Arial")
        
        
     if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}" align="center", font="Arial")
        
        
     # Paddle and ball collisions
          if (ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() -50):
              ball.setx(340)
              ball.dx *= -1
              
          if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and os.system("aplay bounce,wav&")
                                                              



