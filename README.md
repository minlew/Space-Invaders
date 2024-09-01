# Space Invaders Game

## Description
This project is a Python implementation of a Space Invaders-style game using the Turtle graphics library. Players control a spaceship to shoot down alien invaders while avoiding their lasers.

### Features

* Player-controlled spaceship.
* Multiple levels with increasing difficulty.
* Alien fleet that moves and shoots.
* Score tracking.
* Game over screen with final score.

### Technologies
* Python

### Python Libs
* Turtle

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Install [requirements](requirements.txt).
4. Run [script](main.py) in Python. 

## Controls
1. Left Arrow: Move the spaceship left.
2. Right Arrow: Move the spaceship right.
3. Up Arrow: Fire laser.

## Game Rules

* Control your spaceship at the bottom of the screen.
* Shoot down aliens before they reach the bottom.
* Avoid alien lasers.
* The game ends if an alien reaches the bottom or if you're hit by an alien laser.
* Each level introduces a new, faster alien fleet with more frequent laser fire.

## Project Structure
* `main.py`: The main game loop and setup.
* `player.py`: Classes for the player's spaceship and laser.
* `alien_manager.py`: Manages the alien fleet, their movement, and laser firing.
* `score_manager.py`: Handles scoring and level progression.

## Customization
* `alien_manager.py`: Adjust alien movement speed, laser firing rate, etc.
* `player.py`: Modify player movement speed and laser speed
* `score_manager.py`: Change scoring system or level progression
