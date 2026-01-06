import turtle as t 
import os

player_a_score=0
player_b_score=0

# Flag to track if game is running
game_running = True

def on_close():
    global game_running
    game_running = False
  
#create a window and declare a variable called window and call the screen()
window=t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

# Handle window close
window._root.protocol("WM_DELETE_WINDOW", on_close)
  
#Creating the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)


#Creating the right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)
  

#Code for creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ball_dx=0.2
ball_dy=0.2
  
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0",align="center",font=('Arial',24,'normal'))
  
#code for moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+20
    leftpaddle.sety(y)
  
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-20
    leftpaddle.sety(y)
  
#code for moving the rightpaddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+20
    rightpaddle.sety(y)
  
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-20
    rightpaddle.sety(y)
  


#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')
  
while game_running:  # Changed from 'while True'
    window.update()
  
    #moving the ball
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)
  
    #border set up
    if ball.ycor()>290:
        ball.sety(290)
        ball_dy=ball_dy*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball_dy=ball_dy*-1
          
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Arial',24,"normal"))
  
  
    if(ball.xcor()) < -390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Arial',24,"normal"))
  
    # Handling the collisions with paddles.
  
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
  
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1