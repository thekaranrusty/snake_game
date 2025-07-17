from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-260,260)
        self.goto(x,y)
