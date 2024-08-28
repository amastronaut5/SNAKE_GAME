import random
import turtle
from turtle import Turtle


# colours = ["pink","cadetblue","red","orange","blue","grey","white","cyan","magenta","yellow","indigo"]
color_list = [(142, 153, 198), (194, 147, 185), (0,255,255), (240,255,255), (137, 207, 240),(8,143,143), (0,163,108), (204,204,255), (0,128,128), (112,128,144), (192,192,192), (169,169,169), (26, 47, 141), (6, 27, 73), (207, 163, 120), (170, 206, 180), (205, 213, 137), (166, 102, 152), (135, 76, 135), (59, 119, 82), (7, 46, 20), (235, 170, 161), (92, 150, 119), (27, 89, 43), (161, 204, 212), (85, 145, 159), (177, 153, 33), (115, 28, 94), (68, 9, 53), (134, 111, 34),(210,43,43),(222,49,99),(220,20,62) ,(18, 81, 99)]
# r_random = random.randint(0,255)
# g_random = random.randint(0,255)
# b_random = random.randint(0,255)
starting_positions= [(0,0),(0,-20),(0,-40)]
move_dist = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    # screen.colormode(255)
    def __init__(self):

        self.snake_parts = []
        self.COLOR = self.snake_color()
        self.create_snake()
        self.head = self.snake_parts[0]
        # self.user_name = self.screen.textinput(title="Your Name",prompt="WHAT IS YOUR NAME ?")

    def create_snake(self):
        '''creates a snake , uses add_segment function for adding a new part to the snake'''
        for position in starting_positions:
            self.add_segment(position)

    from turtle import Screen
    screen = Screen()

    def snake_color(self):

        self.SNAKE_COL = self.screen.textinput(title="WELCOME TO THE SNAKE GAME !", prompt="WHAT COLOR DO YOU WANT YOUR SNAKE TO BE ?")
        return self.SNAKE_COL



    def add_segment(self,position):
        """adds a new part to the snake everytime it loops through the for loop"""
        # s_col = self.snake_colorsnake_color()
        # print(s_col)


        new_snake_part = Turtle(shape="square")

        if self.COLOR.lower() == "colorful" :
            self.screen.colormode(255)
            new_snake_part.color(random.choice(color_list))
        elif self.COLOR == "":
            new_snake_part.color("white")
        else:
            new_snake_part.color(f"{self.COLOR}")
        new_snake_part.speed(1000)
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.snake_parts.append(new_snake_part)

    def reset(self):
        for part in self.snake_parts:
            part.goto(1000,1000)
        self.snake_parts.clear()
        self.create_snake()
        self.COLOR = self.screen.textinput(title="WELCOME TO THE SNAKE GAME !",
                                               prompt="WHAT COLOR DO YOU WANT YOUR SNAKE TO BE ?")
        self.head = self.snake_parts[0]




    def extend(self):
        '''extends the snake whenever the snake eats the food '''
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        '''Responsible for the movement of snake parts'''
        for no_of_parts in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[no_of_parts - 1].xcor()
            new_y = self.snake_parts[no_of_parts - 1].ycor()
            self.snake_parts[no_of_parts].goto(new_x, new_y)
        self.snake_parts[0].forward(move_dist)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)


    # def user_name(self):
    #     self.screen.textinput(title="Your Name",prompt="WHAT IS YOUR NAME ?")
    #
