from turtle import Turtle

PLAYER_X = 0
PLAYER_Y = -480
PLAYER_MOVE_DISTANCE = 30
LASER_MOVE_DISTANCE = 30


class Player(Turtle):
    def __init__(self):     # Initialize player
        super().__init__()  # Class inheritance. Now player class can do everything a turtle can
        self.shape("triangle")
        self.shapesize(stretch_wid=4, stretch_len=2)
        self.color("lime")
        self.penup()
        self.goto(PLAYER_X, PLAYER_Y)
        self.setheading(90)

    def go_left(self):
        global PLAYER_X
        if self.xcor() > - 870:  # Can't move beyond left edge of screen
            PLAYER_X = PLAYER_X - PLAYER_MOVE_DISTANCE
            self.goto(PLAYER_X, self.ycor())

    def go_right(self):
        global PLAYER_X
        if self.xcor() < 870:  # Can't move beyond right edge of screen
            PLAYER_X = PLAYER_X + PLAYER_MOVE_DISTANCE
            self.goto(PLAYER_X, self.ycor())


class PlayerLaser(Turtle):
    def __init__(self):
        super().__init__()  # Class inheritance. PlayerLaser class can do everything a turtle can
        self.color("white")  # Initially, player laser is "white", this allows create_laser function below to work
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=0.1)
        self.goto(2000, 2000)  # Prevents glitch where initial player_laser turtle destroys an alien

    def create_laser(self):
        if self.color() == ("white", "white"):  # Can only fire laser, when previous laser has disappeared
            self.color("black")
            self.goto(PLAYER_X, PLAYER_Y)

    def laser_move_up(self):
        new_y = self.ycor() + LASER_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # Removes player_laser from play when called
    def laser_disappear(self):
        self.goto(2000, 2000)
