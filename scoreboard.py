from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = ("center")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_score()
        self.hideturtle()
        self.goto(0, 250)

    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)
