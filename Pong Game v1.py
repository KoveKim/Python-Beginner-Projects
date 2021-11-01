# We will NOT be using OOP for this program
import turtle  # Package for graphics. Substitutes the need for Pygame

# Pong game window
window = turtle.Screen()  # This creates the game window
window.title("Pong by Khristian")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Stops window from updating (manual updates). Speeds the game up

# Scorekeeper
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # turtle. is module name, Turtle() is class name
paddle_a.speed(0)  # Set game speed to max
paddle_a.shape("square")
paddle_a.color("salmon")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Wid = Y axis, len = X axis
paddle_a.penup()  # Penup() stops line drawing between shapes
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("light blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball moves on the x/y axis by 2 pixels
ball.dy = 0.2

# Pen (Turtle Module) - Scoring Mechanism
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("RED: 0          BLUE: 0", align="center", font=("Arial", 24, "normal"))


# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()  # ycor() is from Turtle, it returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()  # Listen for keyboard input
window.onkeypress(paddle_a_up, "w")  # We are calling the paddle_a_up function
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")  # Must capitalize for arrow keys
window.onkeypress(paddle_b_down, "Down")


# Every game needs a main game loop, we learned this in game design.
# Main game loop:
while True:
    window.update()  # Every time the loop runs, it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border Checking - Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("RED: {}          BLUE: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("RED: {}          BLUE: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))

    # Paddle collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
