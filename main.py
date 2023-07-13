from turtle import Screen
from player import Player, PlayerLaser
from alien_manager import AlienManager
from score_manager import ScoreManager
import time

# Create a window
screen = Screen()
screen.setup(width=1800, height=1000)
screen.tracer(0)  # Turn off movement animations

# Create various objects from various classes
score_manager = ScoreManager()
player_laser = PlayerLaser()
alien_manager = AlienManager()
player = Player()

screen.listen()  # Get screen to listen for events...
screen.onkey(player.go_left, "Left")  # ...Specifically, key events
screen.onkey(player.go_right, "Right")
screen.onkey(player_laser.create_laser, "Up")

# Create initial set of aliens
alien_manager.create_aliens()

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()  # Turn on periodic screen updates as a replacement for tracer animations

    # Every time screen updates...
    player_laser.laser_move_up()  # ...player laser moves up
    alien_manager.create_alien_laser()  # ...alien fleet has a chance of firing a laser
    alien_manager.laser_move_down()  # ...any alien lasers present will move down
    alien_manager.move_aliens()  # ...alien fleet will move

    # Player laser disappears when it reaches ceiling
    if player_laser.ycor() > 490:
        player_laser.color("white")

    for alien in alien_manager.all_aliens:

        # If any alien reaches the wall, the entire fleet changes direction
        if alien.xcor() > 840 or alien.xcor() < -840:
            if alien.color() != ("white", "white"):
                alien_manager.fleet_bounce()

        # If any reaches the bottom, game over
        if alien.ycor() < -400:
            if alien.color() != ("white", "white"):
                game_is_on = False

        # If player laser hits an alien, alien disappears
        if abs(player_laser.xcor() - alien.xcor()) < 50 and \
                abs(player_laser.ycor() - alien.ycor()) < 50 and \
                alien.color() != ("white", "white"):
            alien.color("white")
            alien.goto(3000, 3000)  # Remove alien from play
            player_laser.color("white")
            player_laser.laser_disappear()  # Prevent laser from hitting multiple aliens
            score_manager.update_running_score()

    # If alien laser hits player, game over
    for alien_laser in alien_manager.all_alien_lasers:
        if abs(player.ycor() - alien_laser.ycor()) < 30 and abs(player.xcor() - alien_laser.xcor()) < 40:
            game_is_on = False

    # If all aliens are shot, next level begins
    if all(alien.color() == ("white", "white") for alien in alien_manager.all_aliens):
        alien_manager.create_aliens()
        score_manager.update_level()

# When game loop is no longer running, final score is  displayed
score_manager.show_final_score()

screen.exitonclick()
