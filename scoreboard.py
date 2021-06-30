from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write_level()

    def write_level(self):
        self.write(arg=f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.home()
        self.color("red")
        self.write(arg="Game Over", align="center", font=FONT)
