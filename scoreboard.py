from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 12, 'normal'))
    def display1(self):
        self.goto(-100, 200)
        self.clear()
        self.write(f' {self.l_score}', move=False,align='center', font=('Courier', 60, 'normal'))
        self.l_score += 1
    def display2(self):
        self.goto(100, 200)
        self.clear()
        self.write(f'{self.r_score}', move=False,align='center', font=('Courier', 60, 'normal'))
        self.r_score += 1