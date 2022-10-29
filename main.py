import random
import time
import turtle
import math

# set up the screen


window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Space invaders")

# create the shapes
turtle.register_shape("images/Space_Invader.gif")
turtle.register_shape("images/player.gif")

# draw the borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(5)
for border in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

# set score
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-290, 280)
score_pen.write("Score: %s" % score, False, align="left", font=("Arial", 16))
score_pen.hideturtle()


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="images/player.gif")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)


# create the player
player = Player()

player_speed = 15
enemy_speed = 4

# create number of enemies
number_of_enemies = 8
enemies = []

# ADD enemies in the list
for i in range(8):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("images/Space_Invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(150, 250)
    enemy.setposition(x, y)


# create firing
class Fire(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="triangle")
        self.color("orange")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()


fire = Fire()
fire_speed = 10


# move the player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    x = player.xcor()
    y = player.ycor() + 10
    fire.setposition(x, y)
    fire.showturtle()


def collision():
    if abs(fire.xcor() - enemy.xcor()) < 30 and abs(fire.ycor() - enemy.ycor()) < 30:
        return True


def game_over():
    distance = math.sqrt(math.pow(player.xcor() - enemy.xcor(), 2) + math.pow(player.ycor() - enemy.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False


# create keyboard events
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    # move the enemies left and right
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        # move enemies back and down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            # move all enemies down
            for i in enemies:
                y = i.ycor()
                y -= 30
                i.sety(y)
            enemy_speed *= -1
        # fire
        fire.forward(fire_speed)
        # check collision between enemies and bullet
        if collision():
            # Score update
            score = score + 1
            score_pen.clear()
            score_pen.write("Score: %s" % score, False, align="left", font=("Arial", 16))
            # reset fire and invader
            fire.hideturtle()
            enemy.hideturtle()
            time.sleep(0.5)
            # update invader and position
            enemy.showturtle()
            x = random.randint(-200, 200)
            enemy.setposition(x, 200)
        if game_over() or enemy.ycor() < -300:
            player.hideturtle()
            fire.hideturtle()
            for e in enemies:
                e.hideturtle()
            window.bgpic("GameOver.gif")
            break