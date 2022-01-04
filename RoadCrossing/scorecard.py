from turtle import Turtle

Font=("Arial",15,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-240,230)
        self.level=1
        self.updatescore()

    def updatescore(self):
        self.write(f"Level:{self.level}",move=False,align='left',font=Font)

    def incrementscore(self):
        self.level+=1
        self.clear()
        self.updatescore()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",move=False,align='Center',font=Font)