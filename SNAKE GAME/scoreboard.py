from turtle import Turtle
from tkinter import *

ALIGNMENT = "center"
FONT = ("calibri", 25, "normal")


class Scoreboard(Turtle):
    # from snake import Snake
    # s = Snake()
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 370)
        self.color("cadetblue")
        self.hideturtle()
        self.update_scoreboard()
        # from turtle import Screen
        # screen = Screen()
        # self.YorN = self.screen.textinput()


    def reset(self):
        if self.score > self.high_score:
            # self.congratulations()
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER ", align=ALIGNMENT, font=("Agency FB",70,"normal"))

    def wanna_conti(self):
        from turtle import Screen
        screen = Screen()
        self.YorN = self.screen.textinput(title="GAME OVER", prompt="DO YOU WANT TO CONTINUE ? TYPE (Y/N)")
        return self.YorN
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 370)
        self.color("cadetblue")
        self.write(f"Your Score : {self.score}     High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()


    def congratulations(self):

        window = Tk()
        window.title("New high score !")
        window.minsize(300,300)
        return Label(text="CONGRATULATIONS ! 🥳🎉 YOU CREATED A NEW HIGH SCORE !",font=("Arial",24,"normal"))





