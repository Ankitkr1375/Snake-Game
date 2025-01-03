from turtle import Turtle
GAMEOVER = ("Arial",24,"normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align="center",font =("Arial",24,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align =ALIGNMENT,font = GAMEOVER)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
