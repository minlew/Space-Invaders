from turtle import Turtle


class ScoreManager(Turtle):
    def __init__(self):     # Initialize player
        super().__init__()  # Class inheritance. Now player class can do everything a turtle can.
        self.score = 0
        self.level = 1
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)  # Hide initial turtle
        self.color("lime")
        self.penup()
        self.goto(-700, 450)
        self.write(
            f"Level: {self.level}    Score: {self.score}", move=False, align="center", font=("Arial", 30, "bold")
        )

    def update_running_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Level: {self.level}    Score: {self.score}", move=False, align="center", font=("Arial", 30, "bold")
        )

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(
            f"Level: {self.level}    Score: {self.score}", move=False, align="center", font=("Arial", 30, "bold")
        )

    def show_final_score(self):
        self.clear()
        self.goto(0, -200)
        self.write(f"Game over!\nYou reached level {self.level}!\nYou shot {self.score} aliens!",
                   move=False, align="center", font=("Arial", 128, "normal"))
