from turtle import Turtle, Screen
import random

LASER_MOVE_DISTANCE = 10
FLEET_X_MOVE_DISTANCE = 1.0
FLEET_Y_MOVE_DISTANCE = 100

# Need to create screen object in order to add custom shapes for Turtle
screen = Screen()
screen.addshape(name="alien.gif", shape=None)


class AlienManager(Turtle):
    def __init__(self):
        super().__init__()  # Class inheritance. Now block class can do everything a turtle can.
        self.all_alien_lasers = []
        self.all_aliens = []
        self.color("white")
        self.penup()
        self.goto(2000, 2000)  # Move initial turtle off game screen
        self.x_start = -500
        self.y_start = -100
        self.x_move = FLEET_X_MOVE_DISTANCE
        self.y_move = FLEET_Y_MOVE_DISTANCE
        self.LASER_SPAWN_RATE = 0

    def create_aliens(self):
        self.all_aliens = []  # Reset alien list each time new level starts in order to reduce lag

        # Reset position each time new fleet is created
        self.x_start = -500
        self.y_start = -100

        self.x_move *= 1.5  # Make fleet faster each time a new one is created
        self.LASER_SPAWN_RATE += 20  # Increase laser spawn rate of aliens with each new fleet

        for i in range(5):  # Move alien factory to the various rows
            self.x_start = -450
            self.y_start = self.y_start + 100
            for j in range(10):  # Print row of aliens at current row
                new_block = Turtle()
                new_block.shape("alien.gif")
                new_block.shapesize(stretch_wid=4, stretch_len=4)
                new_block.penup()
                new_block.goto(self.x_start, self.y_start)
                self.all_aliens.append(new_block)
                self.x_start = self.x_start + 120

    def move_aliens(self):
        for alien in self.all_aliens:
            new_x = alien.xcor() + self.x_move
            alien.goto(new_x, alien.ycor())

    def fleet_bounce(self):
        self.x_move *= -1  # Change direction fleet is moving
        for alien in self.all_aliens:
            new_x = alien.xcor() + self.x_move  # Initial move to prevent glitch
            alien.goto(new_x, alien.ycor())
            new_y = alien.ycor() - self.y_move  # When fleet reaches side and bounces, will also move down
            alien.goto(alien.xcor(), new_y)

    def create_alien_laser(self):
        random_chance = random.randint(self.LASER_SPAWN_RATE, 100)  # Reduce probability of alien fleet firing laser
        if random_chance == 100:
            new_alien_laser = Turtle()
            new_alien_laser.shape("square")
            new_alien_laser.color("black")
            new_alien_laser.shapesize(stretch_wid=1, stretch_len=0.1)
            new_alien_laser.penup()
            new_alien_laser.goto(random.choice(self.all_aliens).pos())  # Laser will spawn a random one of the aliens
            self.all_alien_lasers.append(new_alien_laser)

    def laser_move_down(self):
        for alien_laser in self.all_alien_lasers:
            if alien_laser.ycor() > -510:  # To reduce lag, only move lasers that are still on the screen
                new_y = alien_laser.ycor() - LASER_MOVE_DISTANCE
                alien_laser.goto(alien_laser.xcor(), new_y)
