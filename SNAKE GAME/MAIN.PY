import pygame
pygame.init()

# GAME_SONG = pygame.mixer.Sound("./LEMMiNO.mp3")
BEEP = pygame.mixer.Sound("./beep-sound.mp3")
TXC = pygame.mixer.Sound("./toxic.mp3")
GAME_OVER = pygame.mixer.Sound("./game-over.mp3")

from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

from pause import Pause

def snake_game():
    pause = Pause()

    screen = Screen()

    screen.bgcolor("black")


    screen.screensize(canvwidth = 500,canvheight=500)
    screen.tracer(0)
    x_pos = [0,-20,-40]

    cursor = Turtle()
    cursor.hideturtle()
    cursor.pencolor("white")
    cursor.penup()
    cursor.goto(480,420)
    cursor.pendown()
    cursor.goto(480,-400)
    cursor.goto(-480,-400)
    cursor.goto(-480,420)
    cursor.goto(480,420)


    scoreboard = Scoreboard()

    snake = Snake()
    food = Food()

    #
    # paused = False
    #
    # def unpause():
    #     print("unpause() called")
    #     global paused
    #     paused = False
    #
    # def pause():
    #     global paused
    #     paused = True
    #     while paused:
    #         time.sleep(0.1)




    screen.listen()
    screen.onkeypress(snake.up,"Up")
    screen.onkeypress(snake.down,"Down")
    screen.onkeypress(snake.left,"Left")
    screen.onkeypress(snake.right,"Right")
    # screen.onkeypress(pause.pause_game,"space")
    # screen.onkey(unpause,"space")
    # screen.onkey(scoreboard_reset_highscore,"r")






    score = 0
    game_is_off = False
    game_is_on = True
    while game_is_on:
        # if not pause.paused:

        # GAME_SONG.play()
            screen.update()
            time.sleep(0.1)

            snake.move()




        #collision with food

            if snake.head.distance(food)<20:
                # GAME_SONG.stop()
                BEEP.play()
                food.refresh()
                snake.extend()
                scoreboard.increase_score()


            #DETECT COLLISION WITH THE WALL

            if snake.head.xcor()>460 or snake.head.ycor()>400 or snake.head.xcor()<-475 or snake.head.ycor() < -380:
                # GAME_SONG.stop()
                GAME_OVER.play()
                scoreboard.game_over()

                if scoreboard.wanna_conti().upper() == "Y":
                    TXC.stop()
                    scoreboard.reset()
                    snake.reset()
                    screen.listen()
                    screen.onkeypress(snake.up, "Up")
                    screen.onkeypress(snake.down, "Down")
                    screen.onkeypress(snake.left, "Left")
                    screen.onkeypress(snake.right, "Right")
                else:
                    scoreboard.game_over()
                    game_is_on = False
                    exit()

            #detect collision with tail
            #if head collides with any of the snake parts or segments
            for segment in snake.snake_parts[1:]:
                if snake.head.distance(segment)<10:
                    TXC.play()
                    scoreboard.game_over()
                    # scoreboard.wanna_conti()
                    if scoreboard.wanna_conti().upper() == "Y":
                        TXC.stop()
                        scoreboard.reset()
                        snake.reset()



                        screen.listen()
                        screen.onkeypress(snake.up, "Up")
                        screen.onkeypress(snake.down, "Down")
                        screen.onkeypress(snake.left, "Left")
                        screen.onkeypress(snake.right, "Right")
                    else:
                        scoreboard.game_over()
                        game_is_on = False
                        exit()
        # elif pause.paused:
        #     screen.update()
        #     time.sleep(1)


    # print(score)



    screen.exitonclick()

snake_game()

# import tkinter
# from tkinter import *
#
#
# window = Tk()
# window.title("Game Space")
# window.minsize(width=600,height=600)
#
#
# my_label = tkinter.Label(text = "Welcome! to the Game Space\n"
#                                 "Which game do you want to play ?", font=("Arial",40,"normal"))
# my_label.pack()
#
# button = Button(text="SNAKE GAME",command=snake_game)
# button.pack(side = LEFT)
# window.destroy()
# window.mainloop()