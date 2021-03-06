from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier",24,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        self.score = -1 
        super().__init__()
        self.refresh_score()
       
        
    def refresh_score(self ):
        self.score += 1
        self.reset()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score} " , False , ALIGNMENT, FONT)

    def game_over(self):
        self.goto( 0 , 0 )
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
        