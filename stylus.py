
import turtle

class Stylus(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self,state_name,position):
        self.goto(position)
        self.pendown()
        self.write(state_name)
        self.penup()

