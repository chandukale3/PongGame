from turtle import Turtle, Screen
screen = Screen()
screen.listen()
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid= 5)
        self.penup()
        self.goto(position)
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def move_player1(self):
        screen.onkey(key='Up', fun=self.move_up)
        screen.onkey(key='Down', fun=self.move_down)
    def move_player2(self):
        screen.onkey(key='w', fun=self.move_up)
        screen.onkey(key='s', fun=self.move_down)